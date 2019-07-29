from django import forms
from django.forms import TextInput, Select
from django.db import models
from .models import User


class RegisterForm(forms.ModelForm):
    # 회원가입 폼
    # 장고에서는 HTML 입력요소를 widget(위젯)이라고 말한다.
    password = forms.CharField(label='password',
                widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required' : 'true',
                }))
    confirm_password = forms.CharField(
                    label='confirm password',
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirm Password',
                    'required' : 'true',
                    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required' : 'true',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Firstname',
                'required' : 'true',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
                'required' : 'true',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required' : 'true',
            }),
              'gender': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Gender',
                'required' : 'true',
            }),
        }


    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!')

        return cd['confirm_password']
