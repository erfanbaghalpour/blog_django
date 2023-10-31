from django import template
from ..models import Post, Comment

register = template.Library()


@register.simple_tag(name="total_posts")
def total_posts():
    return Post.published.count()


@register.simple_tag(name="total_comments")
def total_comments():
    return Comment.objects.filter(active=True).count()


@register.simple_tag(name="last_post_date")
def last_post_date():
    return Post.published.last().publish


@register.inclusion_tag("partials/latest_posts.html")
def latest_posts(count=4):
    l_posts = Post.published.order_by('-publish')[:count]
    context = {
        'l_posts': l_posts
    }
    return context
