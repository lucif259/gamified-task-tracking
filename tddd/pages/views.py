from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import CustomUser
from pages.models import Task


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "pages/home.html"

    def get_queryset(self):
        user_id = self.request.user.id
        tasks = super().get_queryset().filter(user_id=user_id, is_complete=False).order_by('-id')
        return tasks

    def post(self, request, *args, **kwargs):
        if request.POST['target'] == 'create':
            Task.objects.create(title=request.POST['title'], user_id=request.user.id)
        elif request.POST['target'] == 'update':
            task = Task.objects.get(id=int(request.POST['id']))
            task.title = request.POST['title']
            task.save()

        return redirect('home')


@api_view(['DELETE'])
def delete_task(request, *args, **kwargs):
    task = Task.objects.get(id=kwargs['id'])
    task.delete()

    return Response(status=200)

@login_required
def some_page(request, *args, **kwargs):

    if request.method == 'POST':
        data = request.POST
        Task.objects.create(title=data['title'], is_complete=False, user_id=request.user.id)

    tasks = Task.objects.all().filter(user_id=request.user.id)

    return render(request, 'pages/some_page.html', {'name': 'Твое имя какая-то ст', 'tasks': tasks})


def current_task(request, *args, **kwargs):
    task = Task.objects.get(id=kwargs['id'])

    if request.method == 'POST':
        data = request.POST
        task.is_complete = data['is_complete'] == 'True'
        task.save()

    return render(request, 'pages/some_current.html', {'task': task})