from django import forms
from .views import post
from .views import comment

# Форма для создания поста
class PostForm(forms.ModelForm):
    class Meta:
        model = post.Post
        fields = ['title', 'content']

# Форма для создания комментария
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment.Comment
        fields = ['content']