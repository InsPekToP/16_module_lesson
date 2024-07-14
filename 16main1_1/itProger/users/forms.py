# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# #чтобы все соединить вместе:

# # class UserRegisterForm(forms.Form):
# # #email = forms.EmailField(required=False) - required=False если не пропишет эмейл,
# # #то форма обработается безе ошибок
# #     email = forms.EmailField(required=True)

# #     class Meta:
# #         models = User
# #         fields = ['email']

# #вместо forms.Form наследуем от UserCreationForm(НЕ РАБОТАЕТ)
# # class UserRegisterForm(UserCreationForm):
# #     email = forms.EmailField(required=True)

# #     class Meta:
# #         models = User
# #         fields = ['email','username','password1','pasword2']

# # class UserRegisterForm(forms.Form):
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(
#         label ='Введите Email',
#         required=True,
#         max_length=100,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите Email'})
#         )
#     username = forms.CharField(
#         label ='Введите логин',
#         required=True,
#         help_text='Нельзя вводить символы: @, /,_',
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Введите логин'})
#         )
#     #выводим в выпадающем меню все обьекты из таблички
#     # some = forms.ModelChoiceField(queryset = User.objects.all())
#     password1 = forms.CharField(
#         label ='Введите пароль',
#         required=True,
#         help_text='Пароль не должен быть маленьким и простым',
#         #отображение в виде точек(для пароля)
#         widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Введите пароль'})
#         )
#     password2 = forms.CharField(
#         label ='Подтвердите пароль',
#         required=True,
#         widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Подтвердите пароль'})
#         )

#     class Meta:
#         models = User
#         fields = ['username','email','some','password1','password2']



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
