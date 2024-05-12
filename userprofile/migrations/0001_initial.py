# Generated by Django 4.2.8 on 2024-05-04 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('e_mail', models.CharField(max_length=255, verbose_name='Электронная почта')),
                ('avatar', models.ImageField(height_field=40, upload_to='userprofile/%Y/%m/%d/', verbose_name='Аватар', width_field=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профайл пользователя',
                'verbose_name_plural': 'Профайл пользователей',
            },
        ),
    ]
