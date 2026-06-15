from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts= Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def post_details(request,id):
    post= get_object_or_404(Post, id=id)
    return render(request,'blog/post_detail.html',{'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request,'blog/create_post.html',{'form':form})

def delete_post(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=='POST':
        post.delete()
        return render(request,'blog/delete_post.html')
    return redirect('home')

def edit_post(request,id):
    post= get_object_or_404(Post,id=id)
    if request.method== 'POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostForm(instance=post)
    return render(request,'blog/edit_post.html',{'form':form})
