from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Логин',
        max_length=50,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=100,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=100
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=100,
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
