# blog/urls.py
from django.urls import path
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),  # URL para listar todos los posts
    path('<int:post_id>/', post_detail, name='post_detail'),  # URL para ver detalles de un post específico
]
