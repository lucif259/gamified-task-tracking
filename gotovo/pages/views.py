from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Task
from accounts.forms import TaskForm
from django.http import JsonResponse
from .models import TaskResponse
from accounts.forms import TaskResponseForm
from accounts.models import UserProfile
from django.views.decorators.csrf import csrf_exempt


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
            task = form.save(commit=False)
            task.user = request.user  # если требуется связать задачу с текущим пользователем
            task.save()
            return redirect('task_list/')
    else:
        form = TaskForm()
    return render(request, 'pages/create_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # если требуется связать задачу с текущим пользователем
            task.save()
            return redirect('completed_tasks')
    return render(request, 'task_list.html', {'tasks': tasks})

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.is_complete = True
        task.save()
        return redirect('task_list')
    return render(request, 'view_task_details.html', {'task': task})

def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    data = {
        'title': task.title,
        'description': task.description,
    }
    return JsonResponse(data)
def complete_task(request):
    # Process form submission and save task response
    # Assuming the form data is processed and saved to the database

    # Redirect to the completed tasks page
    return redirect('completed_tasks')


def completed_tasks(request):
    if request.method == 'POST':
        form = TaskResponseForm(request.POST)
        if form.is_valid():
            task_response = form.save(commit=False)
            task_response.user = request.user
            task_response.save()

            # Обновление рейтинга пользователя
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.rating += 1  # Прибавляем 1 к рейтингу
            user_profile.save()

            return redirect('completed_tasks')
    else:
        form = TaskResponseForm()

    task_responses = TaskResponse.objects.all()
    return render(request, 'completed_tasks.html', {'task_responses': task_responses, 'form': form})