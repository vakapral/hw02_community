from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group
from .models import User
import datetime

POSTS_ON_PAGE = 10


def index(request):
    posts = Post.objects.all()[:POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

def index(request):
    author = User.objects.get(username='leo')
    keyword = 'утро'
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)
    posts = Post.objects.filter(text__contains=keyword).filter(author=author).filter(pub_date__range=(start_date, end_date))

    return render(request, "index.html", {"posts": posts})


# from django.shortcuts import render

# from .models import Post, User
# import logging

# def index(request):
#     log = logging.getLogger('django.db.backends')
#     log.setLevel(logging.DEBUG)
#     log.addHandler(logging.StreamHandler())
#     keyword = request.GET.get("q", None)
#     if keyword:
#         # posts = Post.objects.select_related('author').select_related('group').filter(text__contains=keyword)
#         posts = Post.objects.filter(text__contains=keyword)
#     else:
#         posts = None

#     return render(request, "index.html", {"posts": posts, "keyword": keyword})
