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
