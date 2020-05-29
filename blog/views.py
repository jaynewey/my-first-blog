from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm

def post_list(request):
    search = request.GET.get('q')
    if search and search != "All posts":
        lookups= Q(title__contains=search) | Q(description__icontains=search) | Q(tags__icontains=search)
        posts = Post.objects.filter(lookups).distinct()
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def project_list(request):
    from github import Github
    import json
    from django.contrib.staticfiles.finders import find

    search = request.GET.get('q')
    projects = []
    with open(find("tokens.json")) as tokens:
        g = Github(json.load(tokens)["github"])
        projects = g.get_user().get_repos()
    return render(request, 'blog/project_list.html', {'projects': projects})

def about(request):
    return render(request, 'blog/about.html')
