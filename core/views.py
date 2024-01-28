from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        post = Post.objects.filter(category__name = selected_category)
    else:
        post = Post.objects.all()
    context = {
        'post':post,
        'categories':categories,
        'selected_category':selected_category
    }
    return render(request, 'index.html', context)
    # post = Post.objects.all()
    # context = {
    #     'post':post
    # }
    # return render(request, 'index.html', context)

def get_post(request, pk):
    data = get_object_or_404(Post, pk = pk)
    context = {
        'data':data
    }
    return render(request, 'post_detail.html', context)