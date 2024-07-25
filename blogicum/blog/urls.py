from django.urls import path

from .views import index
from . import views

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='detail'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category'),
]
