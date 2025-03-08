from django.shortcuts import render,redirect

from .models import Post
from .forms import PostForm

def post_list(request):
    posts=Post.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form=PostForm()


      

    context={
        'posts':posts,
        'form':form
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    context={
        'post':post
    }
    return render(request,'blog/post_detail.html',context)
def delete_post(request,slug):
    post=Post.objects.get(slug=slug)
    post.delete()
    return redirect('/blog/')

def update_post(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method=='POST':
        
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form=PostForm(instance=post)
    context={
        'form':form
    }
    return render(request,'blog/update_post.html',context)