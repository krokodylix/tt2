# forms.py
from .models import Post, UserInfo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ['body']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['bio', 'profile_pic']
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 20}),

        }
        labels = {
            'bio': 'Biography',
            'profile_pic': 'Profile Picture'
        }
        help_texts = {
            'bio': 'Tell us about yourself',
            'profile_pic': 'Upload a profile picture'
        }
        error_messages = {
            'bio': {
                'max_length': "This biography is too long.",
            },
        }


