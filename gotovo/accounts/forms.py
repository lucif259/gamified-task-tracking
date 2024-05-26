from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser
from django import forms
from .models import Profile
from pages.models import TaskResponse, Task

class ProfileImageSelectForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['profile_image']
            widgets = {
                'profile_image': forms.RadioSelect
            }
            labels = {
                'profile_image': 'Выберите фотографию профиля'
            }


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'profile_image')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class TaskResponseForm(forms.ModelForm):
    class Meta:
        model = TaskResponse
        fields = ['task', 'response']  # Поля, которые должны быть в форме