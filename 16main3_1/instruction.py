#16main3_1
#Настройка учетной записи и загрузка фотографий

#создадим табличку с разными данными
#    #одна запись в табличке Profile соответсвует 1й записи в табличке User
#on_delete=models.CASCADE - удаляем все вместе с польз-лем
    #user = models.OneToOneField(User,on_delete=models.CASCADE)

#чтобы не было ошибок при выполнении миграций,надо установить библиотеку pillow
#pip install pillow

#после миграций надо импортировать эту табличку в admin.py
# from .models import Profile
# admin.site.register(Profile)

#теперь работаем с картинками,добавили через админ-панель картинку,
# и она появилась у нас в проекте в папке user_images
#теперь делаем,чтобы картинкуи загружались в отдельные папки в settings.py
#MEDIA_URL = '/pictures/' - для браузера,
#он будет понимать из какой папки мы берем картинки
#MEDIA_ROOT = os.path.join(BASE_DIR, 'pictures') - куда закидывать

#src="{{ user.profile.img.url}}" - не работает на локальном серве
#чтобы заработало,надо прописать код в urls.py
# from django.conf import settings
# from django.conf.urls.static import static

#Если находимся в режиме разработки,то в ручном режиме прописываем путь к папке с картинками
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

#теперь при регистрации польз-ль попадает в таблицу User но не попадает в таблицу Profile
#создаем signals.py
#from django.db.models.signals import post_save - отслеживает сохраниение в БД
#from django.dispatch import receiver - декоратор за счет 
#которого мы к методу можем добавить обработчик действия
#@receiver(post_save, sender = User) - отслеживаем табличку User

#НИХРЕНА НЕ ПОНЯТНО!!!!!!!
# @receiver(post_save, sender = User)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)

#instance - зарегистрированый польз-ль

#обновляем инфу о пол-ле
#@receiver(post_save, sender = User)
# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()

#также это все нужно зарегистрировать в apps.py
