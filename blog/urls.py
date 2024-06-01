from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    # path('posts/', views.post_list, name="post_list"),
    path('posts/', views.PostLisView.as_view(), name="post_list"),
    # path('posts/<int:id>', views.post_detail, name="post_detail"),
    path('posts/<int:pk>', views.post_detail, name="post_detail"),
    path('posts/<int:post_id>/comment', views.post_comment, name="post_comment"),
    path('ticket', views.ticket, name="post_detail"),
    path('search/', views.post_search, name="post_search"),
    path('profile/', views.profile, name="profile"),
    path('profile/create-post', views.creat_post, name="creat_post"),
    path('profile/delete-post/<int:post_id>', views.delete_post, name="delete_post"),
]
