from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileImageSelectForm, TaskForm
from pages.views import rating, rating_view
from pages.models import CustomUser
from pages.models import TaskResponse
from .forms import TaskResponseForm


def completed_tasks(request):
    if request.method == 'POST':
        # Создание формы на основе POST-данных
        form = TaskResponseForm(request.POST)
        if form.is_valid():
            # Сохранение ответа в базе данных
            task_response = form.save(commit=False)
            task_response.user = request.user  # Присвоение текущего пользователя
            task_response.save()
            return redirect('completed_tasks')  # Перенаправление на страницу с выполненными задачами
    else:
        # Если запрос не POST, создание пустой формы
        form = TaskResponseForm()

    # Получение всех сохраненных ответов из базы данных
    task_responses = TaskResponse.objects.all()

    # Отображение страницы с выполненными задачами и формой для ввода ответа
    return render(request, 'completed_tasks.html', {'task_responses': task_responses, 'form': form})



@login_required
def profile_image_select(request):
    if request.method == 'POST':
        form = ProfileImageSelectForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправить на страницу профиля пользователя
    else:
        form = ProfileImageSelectForm(instance=request.user.profile)

    return render(request, 'profile_image_select.html', {'form': form})

def rating(request):
    users = CustomUser.objects.all().order_by('-rating')
    return render(request, 'pages/rating.html', {'users': users})

def rating_view(request):
    # Здесь можно добавить логику для получения данных рейтинга и передачи их в шаблон
    return render(request, 'pages/rating.html')

