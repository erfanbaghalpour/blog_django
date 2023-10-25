from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return HttpResponse("index")


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {
        'posts': posts,
    }
    return render(request, "blog/list.html", context)


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404(f"post:{id}")
    context = {
        'posts': post,
    }
    return render(request, "blog/detail.html", context)
