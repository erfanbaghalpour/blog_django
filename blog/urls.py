from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    # path('posts/', views.post_list, name="post_list"),
    path('posts/', views.PostLisView.as_view(), name="post_list"),
    # path('posts/<int:id>', views.post_detail, name="post_detail"),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
]
