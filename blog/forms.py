from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text'] 


class SortPostForm(forms.Form):
    sort_choices = [
        ('update_data', 'По дате обновления'),
        ('category', 'По категории'),
        ('title', 'По заголовку')
    ]

    sort_by = forms.ChoiceField(choices=sort_choices, label='Сортировка по')

