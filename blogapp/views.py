from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import Postform
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blogapp/post_list.html',{'posts' : posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,"blogapp/post_detail.html",{"post" : post})

@login_required
def post_new(request):
    if request.method == 'POST' :
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
        return redirect('blogapp:post_detail',pk=post.pk)
    else:
        form = Postform()
        return render(request,"blogapp/post_edit.html",{"form" : form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
        return redirect('blogapp:post_detail', pk=post.pk)
    else:
        form = Postform()
        return render(request, "blogapp/post_edit.html", {"form": form})

@login_required
def post_management(request):
    if request.method == "POST":
        manage,pk = request.POST["management"].split(" ")
        post = get_object_or_404(Post, pk=pk)
        if manage == "posting" :
            post.publish()
        elif manage == 'private' :
            post.hide()
        elif manage == "modify" :
            return redirect('blogapp:post_edit', pk=pk)
        elif manage == "delate" :
            post.delete()
    posts = Post.objects.all()
    return render(request, 'blogapp/post_management.html', {'posts': posts})