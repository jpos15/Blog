from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Posts
from django.views.generic import ListView


class HomePageView(ListView):
    model = Posts
    template_name = 'app_blog/index.html'


def post_detalhes(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
    except Posts.DoesNotExist:
        raise Http404('Post não encontrado')
    return render(request, 'app_blog/detalhes_post.html', {'post':post})