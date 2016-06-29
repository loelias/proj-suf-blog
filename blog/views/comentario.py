from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic
from django.http import HttpResponse
from blog.models.comentario import Comentario
from blog.models.postagens import Post
from blog.forms import ComentarioForm


def add_comentario_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        print ("ok")
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('post_detail', pk=post.pk)
        else:
            print ("Not ok")
    else:
        form = ComentarioForm()
    return render(request, 'blog/add_comentario_to_post.html', {'form': form})


@login_required
def comentario_aprovado(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.aprovar()
    return redirect('post_detail', pk=comentario.post.pk)


@login_required
def comentario_remover(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    post_pk = comentario.post.pk
    comentario.delete()
    return redirect('post_detail', pk=post_pk)
