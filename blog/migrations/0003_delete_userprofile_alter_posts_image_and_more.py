# Generated by Django 4.2.8 on 2024-05-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_summary_alter_posts_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='blog/%Y/%m/%d/', verbose_name='Изображения', width_field=300),
        ),
        migrations.AlterField(
            model_name='posts',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
    ]
