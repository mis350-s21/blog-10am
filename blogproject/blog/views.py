from django.shortcuts import render

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    c = {
        'post_list': posts,
    }
    return render(request, 'post_list.html', c)


def pub_post_list(request):
    posts = Post.objects.filter(status=1)
    c = {
        'post_list': posts,
    }
    return render(request, 'post_list.html', c)


def unpub_post_list(request):
    posts = Post.objects.filter(status=0)
    c = {
        'post_list': posts,
    }
    return render(request, 'post_list.html', c)


def post_details(request, id):
    p = Post.objects.get(id=id)
    c = {
        'post':p,
    }
    return render(request, 'post_details.html', c)

def post_details_slug(request, s):
    p = Post.objects.get(slug=s)
    c = {
        'post':p,
    }
    return render(request, 'post_details.html', c)
