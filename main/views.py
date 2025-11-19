from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

def home(request):
    data={
        "posts":Post.objects.all()
    }
    
    return render(request,"index.html",context=data)


def detail(request,pk):
    data={
        "post":Post.objects.get(pk=pk)
    }
    
    return render(request,"detail.html",context=data)


def delete(request,pk):
    
    post= get_object_or_404(Post,pk=pk)
    
    if request.method=="POST":
        post.delete()
        return redirect("home")

    
    return render(request,"delete.html",context={"post":post})

def update(request,pk):
    post= get_object_or_404(Post,pk=pk)
    
    if request.method=="POST":
        post.title=request.POST.get("title")
        post.desc=request.POST.get("desc")
        
        if request.FILES.get("image"):
            post.image=request.FILES.get("image")
            
        post.save()
        
        return redirect("home")
    
    return render(request,"edit.html",context={"post":post})

def create(request):
    if request.method=="POST":
        Post.objects.create(
            title=request.POST.get("title"),
            desc=request.POST.get("desc"),
            image=request.FILES.get("image")
        )
        return redirect("home")
    
    return render(request,"create.html")


    
    
    
