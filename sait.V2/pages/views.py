from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from pages.models import Task
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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

def profile_image_select(request, *args, **kwargs):
    return render(request, 'pages/profile_image_select.html')
def street(request, *args, **kwargs):
    return render(request, 'pages/street.html')

def shop(request, *args, **kwargs):
    return render(request, 'pages/shop.html')
def tasking(request, *args, **kwargs):
    return render(request, 'pages/tasking.html')

def CentralStreet(request, *args, **kwargs):
    return  render(request, 'pages/CentralStreet.html')

def rating(request):
    users = CustomUser.objects.all().order_by('-rating')
    return render(request, 'pages/rating.html', {'users': users})

def rating_view(request):
    # Ваш код представления здесь
    return render(request, 'pages/rating.html')

def home(request):
    # Ваш код представления здесь
    return render(request, 'pages/home.html')

def shopi(request):

    return render(request, 'pages/shopi.html')

@login_required
def create_task(request):
    if request.method == 'POST':
        # Логика создания задачи
        task = Task.objects.create(title=request.POST['title'], description=request.POST['description'])
        task.save()
        return redirect('task_list')
    else:
        return render(request, 'pages/create_task.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'GET':
        # Обработка запроса на получение данных о задаче для редактирования
        data = {
            'task_id': task.id,
            'title': task.title,
            'description': task.description,
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        # Обработка запроса на обновление задачи
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return JsonResponse({'success': True})


