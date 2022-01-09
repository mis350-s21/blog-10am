from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import PostForm, CommentForm

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
    f = CommentForm(request.POST or None, initial={
        'post': p.id,
        'author': "Anonymous",
        })
    if f.is_valid():
        f.save()
        return redirect('post_details_slug', s=p.slug)
    
    c = {
        'post':p,
        'comments': cs,
        'form': f,
    }

    return render(request, 'post_details.html', c)

@login_required
def create_post(request):
    f = PostForm(request.POST or None, initial={
        'author': request.user,
    })

    if f.is_valid():
        p = f.save(commit=False)
        print("TITLE IS:",p.title)
        p.slug = slugify(p.title)
        p.save()
        return redirect("post_details_slug", s=p.slug)
    c = {
        'form': f,
    }
    return render(request, 'create_post.html', c)

@login_required
def update_post(request, id):
    p = get_object_or_404(Post, id=id)
    f = PostForm(request.POST or None, instance=p)

    if f.is_valid():
        p = f.save(commit=False)
        print("TITLE IS:",p.title)
        p.slug = slugify(p.title)
        p.save()
        return redirect("post_details_slug", s=p.slug)
    c = {
        'form': f,
    }
    return render(request, 'create_post.html', c)

@login_required
def delete_post(request, id):
    p = get_object_or_404(Post, id=id)
    c = {
        'message': f"delete post {p.title}",
    }
    if "confirm" in request.GET:
        p.delete()
        return redirect('post_list')
    elif "cancel" in request.GET:
        return redirect('post_list')
    return render(request, 'confirm.html', c)