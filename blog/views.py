from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post


def index(request):
    return HttpResponse("index")


def post_list(request):
    posts = Post.published.all()
    context = {
        {'posts': posts},
    }
    return render(request, "", context)


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404(f"post:{id}")
    context = {
        {'posts': post},
    }
    return render(request, "", context)
