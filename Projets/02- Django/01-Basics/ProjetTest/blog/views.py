from django.shortcuts import render
from .models import Post
from django.http import Http404

name_space = 'blog'

# Create your views here.
def index(request):
    posts = Post.objects.all()
    print(posts.__len__)
    return render(request, 'blog/index.html', { 'posts' : posts })

def details(request, id_url):
    try:
        post = Post.objects.get(id=id_url)
    except Post.DoesNotExist:
        raise Http404("Le poste que vous avez demandé n'existe pas")

   
    return render(request, 'blog/pages/details.html', { 'post' : post } )

