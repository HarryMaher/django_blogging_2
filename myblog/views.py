from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from myblog.models import Post
# Create your views here. 

# Collect subject matter to be displayed


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')

    return render(request, 'list.html', {'posts':posts})

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'detail.html', context)
