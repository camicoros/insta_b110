from django import forms

from .models import Post


class PostForm(forms.Form):
    name = forms.CharField(
        label="Название",
        max_length=80,
        required=True,
    )

    image = forms.ImageField(label="Картинка", required=True)
    description = forms.CharField(label="Описание", max_length=1000)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'image', 'description']
