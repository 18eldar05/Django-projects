from .models import Comment
from django.forms import ModelForm, TextInput, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text", "surname", "photo"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'contacts_input',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'contacts_input',
                'placeholder': 'Фамилия'
            }),
            "text": Textarea(attrs={
                'class': 'contacts_textarea',
                'placeholder': 'Комментарий'
            })
        }
