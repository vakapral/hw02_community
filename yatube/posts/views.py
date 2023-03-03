from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # description = get_object_or_404(Group, description=description)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        # 'description': description,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
