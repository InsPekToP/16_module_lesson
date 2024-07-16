#16main1_1
#Авторизация и выход из учетной записи

#надо добавить отслеживание дополнительных url-адресов в urls.py(itProger)
    # path('user/',authViews.LoginView.as_view(template_name = 'users/user.html'), name='user'),
    # path('exit/',authViews.LogoutView.as_view(), name='exit'),
#template_name = 'users/user.html' - надо передавать

#в папке users делаем шаблон user.html

#после авторизации надо отпрвлять поль-ля на главную страницу
#для этого в  settings.py добавляемм LOGIN_REDIRECT_URL = 'home'

#теперь через сайт можем авторизироваться в админ-панели

#создаем exit.html
