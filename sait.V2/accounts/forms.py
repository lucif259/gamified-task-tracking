from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser
from django import forms
from .models import Profile

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
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', )