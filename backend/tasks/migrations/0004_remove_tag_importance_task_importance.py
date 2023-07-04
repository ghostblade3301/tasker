# Generated by Django 4.2.2 on 2023-07-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tag_options_alter_tag_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='importance',
        ),
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.CharField(choices=[('CRITICAL', 'Critical'), ('HIGH', 'High'), ('NORMAL', 'Normal')], default=1, max_length=25, verbose_name='Важность'),
            preserve_default=False,
        ),
    ]
