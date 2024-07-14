from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
#создавать разные типы сообщений


# def register(request):
#     form = UserCreationForm()
#     return render(
#         request,
#         'users/registration.html',
#         {
#             'title':'Страница регистрации',
#             'form':form
#             })

#теперь вместо стандартного класса UserCreationForm подставляем свой UserRegisterForm

def register(request):
    #если данные передаются методом post
    if request.method == "POST":
        #здесть будут храниться все данные полученные от польз-ля
        form = UserRegisterForm(request.POST)
        #проверка на правильность данных
        if form.is_valid():
#чтобы сохранять зарегистрированых пользователей в БД надо эту строчку раскоментить
            # form.save()
            #очищенные данные(не понятно)
            username = form.cleaned_data.get('username')
            #messages.info()
            # messages.error()
            # messages.warning()
            messages.success(request,f'Пользователь {username} был успешно создан!')
            #теперь надо перебросить поль-ля на другую страницу
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'title':'Страница регистрации',
            'form':form
            }
        )
