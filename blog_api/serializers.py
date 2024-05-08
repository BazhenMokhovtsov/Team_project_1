import datetime

from rest_framework import serializers
from pytils.translit import slugify

from blog.models import Category, Post, Comments


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
    slug = serializers.SlugField(read_only=True, required=False)

    class Meta:
        model = Post
        fields = ['pk', 'author', 'category', 'title', 'text', 'update_date', 'published',
                  'image', 'slug']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        validated_data['update_date'] = datetime.datetime.utcnow()
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.update_date = datetime.datetime.utcnow()
        instance.published = validated_data.get('published', instance.published)
        instance.image = validated_data.get('image', instance.image)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['author', 'post', 'text', 'created_date']
        depth = 1

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)

