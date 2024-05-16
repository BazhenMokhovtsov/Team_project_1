from django.db import models
from pytils.translit import slugify
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

    
class Posts(models.Model):
    text = models.TextField(verbose_name="Текст")
    summary = models.CharField(max_length=200, blank=True)
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, default=User, null=True)
    update_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    create_date = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    published = models.BooleanField(verbose_name="Публикация", default=False)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображения", upload_to='blog/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField(verbose_name='Слаг',max_length=200)

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = "Пост/Новость"
        verbose_name_plural = "Посты/Новости"
        ordering = ['-create_date']
        indexes = [ models.Index(fields=['create_date'])]


    def save(self, *args, **kwargs):                
        self.summary = self.text[:200]
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        super(Posts, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    
class Comments(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, verbose_name="Пост/Новость", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateTimeField(verbose_name="Дата добавления коментария", auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    class Meta:
         verbose_name = "Коментарий"
         verbose_name_plural = "Коментарии"

    