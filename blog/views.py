from django.shortcuts import render
from django.utils import timezone
from .models import Postear
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Postear.objects.filter(Fecha_de_Publicacion__lte=timezone.now()).order_by('Fecha_de_Publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detalle(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detalle.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Autor = request.user
            post.save()
            return redirect('blog.views.post_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.Autor = request.user
            post.save()
            return redirect('blog.views.post_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
