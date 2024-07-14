#16main1_1
#Добавление регистрации

#создаем новое приложение
#python manage.py startapp users
#регистрируем приложение в INSTALLED_APPS - 'users.apps.UsersConfig'

#так тоже можно подклучать url,но лучше делать по старому
#from users import views as userViews
#path('reg',userViews.register),

#пользуемся встроенным классом в Django для создание регистрации
#from django.contrib.auth.forms import UserCreationForm

#{{form.as_p}} as_p - фильтр,кот. говорит,что каждая форма выводится как 
#отдельный параграф

#type="submit" - при нажатии - перезагрузка страницы

#ключ безопасности{{ csrf_token }}
#{% csrf_token %} - не видно ключ

#для емейла создаем forms.py
#email = forms.EmailField(required=False) - required=False если не пропишет эмейл,
#то форма обработается без ошибок

#widget=forms.PasswordInput - отображение в виде точек(для пароля)
#подставить стили от Bootstrap
#PasswordInput(attrs={'class':'form-control'})

#TextInput - для текста
#widget=forms.TextInput(attrs={'class':'form-control'})

#получаем данные от пол-ля в views.py
#import redirect - переброс на другую страницу

#чтобы сохранять зарегистрированых пользователей в БД надо эту строчку раскоментить
#form.save() - выбивает ошибку,т.к. надо прописать такой метод как 
#save(), поэтому надо исп-ть метод UserCreationForm