from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    username_field = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'phone']

    def create_user(self, email, first_name, last_name, phone, password=None, role="user"):
        """
        функция создания пользователя — в нее мы передаем обязательные поля
        """

        if not email:
            raise ValueError('Пользователь должен указать email')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None, **kwargs):
        """
        функция для создания суперпользователя — с ее помощью мы создаем администратора
        это можно сделать с помощью команды createsuperuser
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=kwargs.get('role')
        )

        return user
