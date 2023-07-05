from django.contrib import admin

from .models import Tag, Task, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'description',
        'image',
        'created_at',
        'is_completed',
        'importance',
        'executor',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'task',
        'author',
        'text',
        'created_at',
    )
