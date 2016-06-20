from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by(
        'data_publicacao')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(data_publicacao__isnull=True).order_by(
        'data_criacao')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publica()
    return redirect('blog.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


def add_comentario_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog/add_comentario_to_post.html', {'form': form})


@login_required
def comentario_aprovado(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.aprovar()
    return redirect('blog.views.post_detail', pk=comentario.post.pk)


@login_required
def comentario_remover(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    post_pk = comentario.post.pk
    comentario.delete()
    return redirect('blog.views.post_detail', pk=post_pk)
