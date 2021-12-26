from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('published/', views.pub_post_list, name="pub_post_list"),
    path('draft/', views.unpub_post_list, name="unpub_post_list"),
    path('post/<int:id>/', views.post_details, name='post_details'),
    path('post/<str:s>/', views.post_details_slug, name='post_details_slug'),
    path('create/post/', views.create_post, name='create_post'),
]