from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    first_name =models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    birth_date = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    city = models.CharField(verbose_name="Город", max_length=50)
    e_mail = models.CharField(verbose_name="Электронная почта", max_length=255)
    avatar = models.ImageField(verbose_name="Аватар", upload_to='userprofile/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = "Профайл пользователя"
        verbose_name_plural = "Профайл пользователей"

    def save(self,*args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 75 or img.width > 75:
                output_size = (75, 75)
                img.thumbnail(output_size)
                img.save(self.avatar.path)
    
    