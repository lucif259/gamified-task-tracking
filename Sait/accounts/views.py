from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileImageSelectForm

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
