from django.urls import path
#из этой же директории импорт views.py(в той же папке находится)
from . import views

urlpatterns = [
#в Django ссылки принято еще называть,теперь в base.html можем исп-ть шаблонизатор
# джинджер.Тоесть писать вместо href="/">Главная</a> вставить ссылку на имя
#href="{% url 'home' %}">Главная</a>
    path('',views.home, name='home'),
    # path('contacti',views.contacti, name='contacti')
#теперьполучается большая вариативность.Например хочу чтобы вызывалось не по contacti,
# а по about 
    path('about',views.contacti, name='contacti')
]