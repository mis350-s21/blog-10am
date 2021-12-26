from django.shortcuts import render, get_object_or_404, redirect

from .models import Post

from .forms import PostForm

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
    # p = Post.objects.get(id=id)
    p = get_object_or_404(Post, id=id)
    c = {
        'post':p,
    }
    return render(request, 'post_details.html', c)

def post_details_slug(request, s):
    
    p = Post.objects.get(slug=s)
    cs = p.comment_set.all()

    c = {
        'post':p,
        'comments': cs,
    }
    return render(request, 'post_details.html', c)

def create_post(request):
    f = PostForm(request.POST or None)

    if f.is_valid():
        f.save()
        return redirect("post_list")
    c = {
        'form': f,
    }
    return render(request, 'create_post.html', c)
