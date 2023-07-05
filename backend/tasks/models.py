from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Tag (models.Model):

    name = models.CharField(
        max_length=25,
        verbose_name='Тэг',
        unique=True,
        blank=False
    )

    slug = models.CharField(
        max_length=25,
        verbose_name='Слаг',
        unique=True,
        blank=False
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Task(models.Model):

    IMPORTANCE = (
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('NORMAL', 'Normal'),
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Название задания',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Автор задания',
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Описание задания',
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='tasks/',
        blank=True,
        )
    created_at = models.DateTimeField(
        verbose_name='Создано в',
        auto_now_add=True,
    )
    is_completed = models.BooleanField(
        verbose_name='Статус выполнения',
    )
    importance = models.CharField(
        verbose_name='Важность',
        max_length=25,
        choices=IMPORTANCE,
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
    )

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    text = models.TextField(
        max_length=500,
        verbose_name='Текст комментария',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания комментария',
        auto_now_add=True,
    )

    def __str__(self):
        return self.text[:15]
