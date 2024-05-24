from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from accounts.models import Task
from accounts.forms import TaskForm

@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "pages/home.html"

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

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Предположим, что у вас есть URL-адрес для списка задач
    else:
        form = TaskForm()
    return render(request, 'pages/create_task.html', {'form': form})

def completed_tasks(request):
    completed_tasks = Task.objects.filter(is_complete=True)
    return render(request, 'pages/completed_tasks.html', {'completed_tasks': completed_tasks})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'pages/task_list.html', {'tasks': tasks})