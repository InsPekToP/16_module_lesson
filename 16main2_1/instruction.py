#16main2_1
#Авторизация и выход из учетной записи

#надо добавить отслеживание дополнительных url-адресов в urls.py(itProger)
    # path('user/',authViews.LoginView.as_view(template_name = 'users/user.html'), name='user'),
    # path('exit/',authViews.LogoutView.as_view(), name='exit'),
#template_name = 'users/user.html' - надо передавать

#в папке users делаем шаблон user.html

#после авторизации надо отпрвлять поль-ля на главную страницу
#для этого в  settings.py добавляемм LOGIN_REDIRECT_URL = 'home'

#теперь через сайт можем авторизироваться в админ-панели

#создаем exit.html копируем в него все от user.html

#теперь делаем разные кнопки для авторизованых и не авторизованых поль-лей

#для выхода из системы
#   <form action="{% url 'exit' %}" class="ml-2" method="post">
#               {% csrf_token %}
#               <button type="submit" class="btn btn-outline-info">Выйти</button>
#             </form>


#отслеживание профиля пользователя в urls.py
#path('profile/',userViews.profile, name='profile'),

#создаем новую ф-ию в views.py
#def profile(request):
    #return render(request, 'users/profile.html')
#теперь надо сделать,чтобы эту страницу было видно только зарег. пол-лям
#делаем декоратор(@login_required)
#from django.contrib.auth.decorators import login_required
#перекидывает не туда куда нужно,для этого в settings.py пишем LOGIN_URL = 'user'