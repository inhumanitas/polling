# coding=utf-8
from django import forms


class UserRegistrationForm(forms.Form):
    widget = forms.Select()
    first_name = forms.CharField(label=u'Имя', max_length=20)
    last_name = forms.CharField(label=u'Фамилия', max_length=20)
    username = forms.CharField(label=u'Логин', max_length=20)
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label=u'Пароль(снова)', widget=forms.PasswordInput())
    email = forms.EmailField(label=u'Почтовый ящик')
    pasport_data = forms.CharField(label=u'Паспортные данные', max_length=200)