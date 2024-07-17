#16main4_1
#Изменение профиля на сайте

#работаем с forms.py
#создали 2 класса class UserUpdateForm(forms.Form): - раобновляет эмейл
#и работает с табличкой  User   class Meta:
        #model = User

#class ProfileImageForm(forms.Form):- обновляет картинку 
#и работает с таблицой Profile     class Meta:
        # model = Profile
        # fields = ['img']

#в views.py в profile дописываем создание обьектов на основе этих форм
# @login_required
# def profile(request):
#     profileForm = ProfileImageForm()
#     updateUserForm = UserUpdateForm()

#     data = {
#         'profileForm': profileForm,
#         'updateUserForm':updateUserForm
#     }

#     return render(request, 'users/profile.html',data)

#profileForm = ProfileImageForm(instance=request.user.profile) - чтобы выводилось,
#то что польз-ль вводил раньше(ВЫБИВАЕТ ОШИБКУ)
#чтобы этого не было нужно вместо forms.Form подставить form.ModelForm

#теперь добавляем отображение этих форм в файле profile.html

#enctype="multipart/form-data" - надо добавлять в форму,чтобы 
#нормально работать с изображениями

#чтобы контролировать размер файла,кот. грузят пол-ли
#надо написать проверку,а затем орезать в папке models.py