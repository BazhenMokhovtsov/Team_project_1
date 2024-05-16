# Generated by Django 4.2.8 on 2024-05-16 12:33

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('published', models.BooleanField(default=False, verbose_name='Публикация')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d/', verbose_name='Изображения')),
                ('slug', models.SlugField(max_length=200, verbose_name='Слаг')),
                ('author', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Пост/Новость',
                'verbose_name_plural': 'Посты/Новости',
                'ordering': ['-update_date'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления коментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.posts', verbose_name='Пост/Новость')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.AddIndex(
            model_name='posts',
            index=models.Index(fields=['update_date'], name='blog_posts_update__392ed1_idx'),
        ),
    ]
