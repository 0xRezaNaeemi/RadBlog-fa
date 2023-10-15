from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<int:id>', views.post_detail, name='post_detail'),
]
