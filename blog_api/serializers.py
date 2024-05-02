import datetime

from rest_framework import serializers
from pytils.translit import slugify

from blog.models import Category, Posts, Comments


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(allow_null=True, required=True)

    class Meta:
        model = Category
        fields = ['pk', 'url', 'title', 'slug']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(allow_null=True, required=False)
    image = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Posts
        fields = ['pk', 'author', 'category', 'title', 'text', 'update_date', 'published',
                  'image', 'slug']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        validated_data['update_date'] = datetime.datetime.utcnow()
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.title)
        instance.category = validated_data.get('category', instance.title)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.title)
        instance.update_date = datetime.datetime.utcnow()
        instance.published = validated_data.get('published', instance.title)
        instance.image = validated_data.get('image', instance.title)
        instance.title = slugify(instance.title)
        instance.save()
        return instance
