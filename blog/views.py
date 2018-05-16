from django.shortcuts import render

# Create your views here.

def index_page(request):
    # The function render will render (put together) our template blog/post_list.html
    return render(request, 'blog/index.html', {})

def about_page(request):
    return render(request, 'blog/about.html', {})