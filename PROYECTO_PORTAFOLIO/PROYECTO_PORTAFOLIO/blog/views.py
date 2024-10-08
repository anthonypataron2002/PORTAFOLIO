# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def render_posts(request):
    posts = Post.objects.all()  # Obtener todos los posts
    return render(request, 'blog/posts.html', {'posts': posts})  # Pasar los posts al template
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # Recuperar el post específico o devolver 404 si no existe
    return render(request, 'blog/post_detail.html', {'post': post})  # Asegúrate de tener un template para post_detail
