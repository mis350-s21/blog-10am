from django.urls import path

from .views import post_list, pub_post_list, unpub_post_list

urlpatterns = [
    path('', post_list, name="post_list"),
    path('published/', pub_post_list, name="pub_post_list"),
    path('draft/', unpub_post_list, name="unpub_post_list"),
    
]