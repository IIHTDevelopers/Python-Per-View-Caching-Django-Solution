# views.py
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import BlogPost

@cache_page(60 * 15)  # Cache for 15 minutes
def blog_post_detail(request, post_id):
    """View to display the blog post detail page."""
    post = BlogPost.objects.get(id=post_id)
    # return HTT
    return render(request, 'blog_detail.html', {'post': post})
