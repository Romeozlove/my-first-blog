from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


<<<<<<< HEAD
@login_required()
=======
>>>>>>> 655399f5ad88004078cd61d56d6d6a0db2f89d11
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


<<<<<<< HEAD
@login_required()
=======
>>>>>>> 655399f5ad88004078cd61d56d6d6a0db2f89d11
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


<<<<<<< HEAD
@login_required()
=======
>>>>>>> 655399f5ad88004078cd61d56d6d6a0db2f89d11
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


<<<<<<< HEAD
@login_required()
=======
>>>>>>> 655399f5ad88004078cd61d56d6d6a0db2f89d11
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


<<<<<<< HEAD
@login_required()
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
=======
def post_remove(request, pk):
    post = get_o bject_or_404(Post, pk=pk)
>>>>>>> 655399f5ad88004078cd61d56d6d6a0db2f89d11
    post.delete()
    return redirect('post_list')
