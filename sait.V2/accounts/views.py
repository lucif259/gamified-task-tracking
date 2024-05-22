from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileImageSelectForm
from pages.views import rating, rating_view
from pages.models import CustomUser
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