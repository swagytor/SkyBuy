from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, "Пользователь"),
        (ADMIN, "Администратор")
    )


class User(AbstractBaseUser):
    objects = UserManager()

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", )
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER, verbose_name="Роль")
    image = models.ImageField(upload_to="users/", null=True, blank=True, verbose_name="Изображение")

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'phone']

    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
