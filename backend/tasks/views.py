from django.shortcuts import render, get_object_or_404

from .models import Comment, Tag, Task


def index(request):
    template = 'tasks/index.html'
    task_list = Task.objects.all()
    context = {
        'task_list': task_list,
    }
    return render(request, template, context)
