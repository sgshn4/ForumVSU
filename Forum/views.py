from django.shortcuts import render, get_object_or_404, redirect
from . import post
from . import comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Отображение всех постов
def post_list(request):
    posts = post.Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

# Просмотр одного поста с комментариями
def post_detail(request, pk):
    post_unit = get_object_or_404(post.Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

# Создание нового поста (требует авторизации)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})