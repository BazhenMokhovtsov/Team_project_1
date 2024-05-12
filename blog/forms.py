from django import forms
from .models import Comments, Posts

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['text']  # Включить только указанные поля


class SortPostForm(forms.Form):
    sort_choices = [
        ('update_data','По дате обновления'),
        ('title','По заголовку'),
        ('category', 'По категории')
    ]

    sort_by = forms.ChoiceField(choices=sort_choices, label='Сортировка по')


