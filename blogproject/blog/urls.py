from django.urls import path

from .views import post_list, pub_post_list, unpub_post_list, post_details, post_details_slug

urlpatterns = [
    path('', post_list, name="post_list"),
    path('published/', pub_post_list, name="pub_post_list"),
    path('draft/', unpub_post_list, name="unpub_post_list"),
    path('post/<int:id>/', post_details, name='post_details'),
    path('post/<str:s>/', post_details_slug, name='post_details_slug'),
]