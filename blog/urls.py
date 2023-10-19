from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # path('blog/', views.post_list, name='post_list'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    # path('blog/<int:id>', views.post_detail, name='post_detail'),
    path('blog/<pk>', views.PostDetailView.as_view(), name='post_detail'),
]
