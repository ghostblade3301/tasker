# Generated by Django 4.2.2 on 2023-07-05 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_alter_task_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
            preserve_default=False,
        ),
    ]
