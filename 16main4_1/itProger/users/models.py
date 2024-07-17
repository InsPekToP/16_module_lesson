from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    #одна запись в табличке Profile соответсвует 1й записи в табличке User
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя',default='default.png',upload_to='user_images')


#чтобы все файлы нормально отображались
    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
    
    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'