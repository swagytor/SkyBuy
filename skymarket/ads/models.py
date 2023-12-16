from django.db import models

from users.models import User

NULLABLE = {
    'null': True,
    'blank': True
}


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.ImageField(upload_to="ads/", **NULLABLE, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление", related_name="comments")

    def __str__(self):
        return f'{self.ad.title} - {self.author}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
