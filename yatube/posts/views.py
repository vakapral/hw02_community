from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
# from .models import Group
# from .models import User
# import datetime
from django.core.paginator import Paginator


POSTS_ON_PAGE = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts = page_obj.object_list
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts = page_obj.object_list
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    post_list = user.posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts = page_obj.object_list
    post_count = user.posts.all().count()
    context = {
        'user': user,
        'posts': posts,
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author = post.author
    post_count = Post.objects.all().filter(author=author).count()
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    # context = {
    #     'form': postForm,
    #     'post_count': post_count,
    # }
    return render(request, 'posts/create_post.html')



# def index(request):
#     author = User.objects.get(username='leo')
#     keyword = 'утро'
#     start_date = datetime.date(1854, 7, 7)
#     end_date = datetime.date(1854, 7, 21)
#     posts = Post.objects.filter(text__contains=keyword).filter(author=author).filter(pub_date__range=(start_date, end_date))

#     return render(request, "index.html", {"posts": posts})


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
