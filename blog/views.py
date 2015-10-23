from django.shortcuts import render
from django.utils import timezone
from .models import Postear
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Postear.objects.filter(Fecha_de_Publicacion__lte=timezone.now()).order_by('Fecha_de_Publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detalle(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detalle.html', {'post': post})
