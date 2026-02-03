from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost
from .forms import BlogpostForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('home')
    else:
        form = BlogpostForm()
    return render(request, 'create_post.html', {'form': form})

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})


def logout_view(request):
    logout(request)
    return redirect('home')


def create_post(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('home')
    else:
        form = BlogpostForm()
    return render(request, 'create_post.html', {'form': form})

def post_view(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def update_post(request, pk):
    post = BlogPost.objects.get(pk=pk, author=request.user)
    if request.method == 'POST':
        form = BlogpostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Blog post updated successfully!')
            return redirect('post_view', pk=post.pk)
    else:
        form = BlogpostForm(instance=post)
    return render(request, 'update_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = BlogPost.objects.get(pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        # messages.success(request, 'Blog post deleted successfully!')
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})