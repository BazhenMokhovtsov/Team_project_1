from django.db import models
from pytils.translit import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self):
        if not self.slug:
            self.slug = slugify(self.slug)
            super().save()

    
class Posts(models.Model):
    text = models.TextField(verbose_name="Текст")
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, default=User)
    update_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    published = models.BooleanField(verbose_name="Публикация", default=False)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображения", upload_to=None, height_field=300, width_field=300, max_length=None)
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = "Пост/Новость"
        verbose_name_plural = "Посты/Новости"

    def save(self):
        if not self.slug:                       
            self.slug = slugify(self.slug)
            super().save()

    
class Comments(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, verbose_name="Пост/Новость", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateTimeField(verbose_name="Дата добавления коментария", auto_now_add=True)