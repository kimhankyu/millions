#community/views.py

from django.shortcuts import render, render,get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import Post
# from users.models import User
from django.utils import timezone
from .forms import NewPost

# Create your views here.

def community(request):
    posts = Post.objects.all()
    return render(request, 'community.html', {'posts':posts})

def detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'community/detail.html', {'detail': detail})

@login_required
def new_post(request):
    return render(request, 'new_post.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid:
            new_post = form.save(commit=False)
            new_post.created = timezone.now()
            new_post.save()
            return redirect('community')
        else:
            form = NewPost()
            return render(request, 'community/new.html', {'form': form})
    # new_post = Post()
    # new_post.title = request.GET['title']
    # new_post.image = request.GET['image']
    # new_post.body = request.GET['body']
    # new_post.created = timezone.datetime.now()
    # new_post.save()
    
@login_required
def update(request, post_id):
    
    # 어떤 블로그를 수정할지 블로그 객체를 갖고오기
    posting = get_object_or_404(Post, pk = post_id)
    
    # 해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewPost(request.POST, instance=posting)
    
    if form.is_valid():
        form.save()
        return redirect('community')

    return render(request, 'community/new.html', {'form':form})
    
@login_required    
def delete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('community')