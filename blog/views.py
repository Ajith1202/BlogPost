from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    objects = BlogPost.objects.all().order_by('-created_on')

    context = {'objects':objects,}
    return render(request, 'blog/home.html', context)


def update_blog(request, pk):
    obj = BlogPost.objects.get(id=pk)

    form = BlogPostForm(instance=obj)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'obj':obj, 'form':form}

    return render(request, 'blog/update.html', context)    


def create_blog(request):
    form = BlogPostForm()

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    context = {'form':form}          
    return render(request, 'blog/create.html', context)        

def detail_page(request, pk):
    obj = BlogPost.objects.get(id=pk)

    context = {'obj':obj}
    return render(request, 'blog/detail.html', context)

def delete_blog(request, pk):
    obj = BlogPost.objects.get(id=pk)

    obj.delete()
    return redirect('home')

def search_blog(request):
    if request.method == 'POST':
        search = request.POST.get('search')

    obj = BlogPost.objects.all().filter(title__icontains=search)
    length = len(obj)
    context = {'obj':obj, 'length':length}

    return render(request, 'blog/search.html', context)
