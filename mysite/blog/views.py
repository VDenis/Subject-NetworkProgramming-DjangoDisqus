from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post
