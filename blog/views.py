from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.contrib.postgres.search import SearchVector


def index(request):
    return render(request, "blog/index.html")


# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     context = {
#         'posts': posts,
#     }
#     return render(request, "blog/list.html", context)

class PostLisView(ListView):
    # model = Post
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/list.html'


def post_detail(request, pk):
    # try:
    #     post = Post.published.get(id=id)
    # except:
    #     raise Http404(f"post:{id}")
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        'posts': post,
        'form': form,
        'comments': comments,
    }
    return render(request, "blog/detail.html", context)


# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = "blog/detail.html"


def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cd = form.cleaned_data
            ticket_obj.message = cd['message']
            ticket_obj.name = cd['name']
            ticket_obj.email = cd['email']
            ticket_obj.phone = cd['phone']
            ticket_obj.subject = cd['subject']
            ticket_obj.save()
            return redirect("blog:index")
    else:
        form = TicketForm()

    return render(request, 'forms/ticket.html', {'form': form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    context = {
        'post': post,
        'form': form,
        'comment': comment,
    }
    return render(request, "forms/comment.html", context=context)


def post_search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # results = Post.published.filter(Q(description__icontains=query) | Q(title__icontains=query))
            results = Post.published.annotate(search=SearchVector('title', 'description', 'slug')).filter(search=query)
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)
