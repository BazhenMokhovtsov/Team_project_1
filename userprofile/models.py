from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    first_name =models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    birth_date = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    city = models.CharField(verbose_name="Город", max_length=50)
    e_mail = models.CharField(verbose_name="Электронная почта", max_length=255)
    avatar = models.ImageField(verbose_name="Аватар", upload_to='userprofile/%Y/%m/%d/', height_field=40, width_field=40)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = "Профайл пользователя"
        verbose_name_plural = "Профайл пользователей"
    