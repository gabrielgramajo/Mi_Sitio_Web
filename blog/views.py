from django.shortcuts import render
from django.utils import timezone
from .models import Postear

def post_list(request):
    posts = Postear.objects.filter(Fecha_de_Publicacion__lte=timezone.now()).order_by('Fecha_de_Publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})
