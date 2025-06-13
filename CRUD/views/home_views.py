from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import Blogs
from ..models import Contact as  Contact_models

# Create your views here.
def Home(request):
    blogs = Blogs.objects.all()[0:6]
    return render(request,"home.html",{"blogs":blogs})

@login_required
def Create_blog(request):
    if request.method == "POST":
        author = request.user.username
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("content")
        tags = request.POST.get("tags")
        image = request.FILES.get("image")  # ✅ Correct key name

        blog = Blogs(
            title=title,
            subtitle=subtitle,
            description=description,
            tags=tags,
            image=image,
            author = author
        )
        blog.save()
        return redirect("home")  # or your desired page

    return render(request, "create_blog.html")

def Single_blog(request,blog_id):
    single_data = get_object_or_404(Blogs,pk = blog_id )
    return render(request,"single_page.html",{'single_data':single_data})


@login_required
def Your_blogs(request):
    
    user = request.user
    blogs = Blogs.objects.filter(author = user)
    
    
    return render(request,"your_blogs.html",{'blogs':blogs})

@login_required
def Delete_blog(request,blog_id):
    
    if request.method == "POST":
        blog = get_object_or_404(Blogs,pk = blog_id)
        blog.delete()
    
    return redirect("Your_blogs")

@login_required
def Edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id, author=request.user)

    if request.method == "POST":
        blog.title = request.POST.get("title")
        blog.subtitle = request.POST.get("subtitle")
        blog.description = request.POST.get("content")
        blog.tags = request.POST.get("tags")

        # Only update the image if a new one was uploaded
        if request.FILES.get("image"):
            blog.image = request.FILES.get("image")

        blog.save()
        return redirect("Your_blogs")  # ✅ Redirect after POST

    return render(request, "edit_blog.html", {'blog': blog})  # ✅ Render correct edit template

def Read_blog(request):
    
    blogs = Blogs.objects.all().order_by('-created_at')
    
    return render(request, "read_blog.html", {'blogs':blogs})

def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        contact = Contact_models(
            name = name,
            email = email,
            message = message
        )
        
        contact.save()
        
        return redirect(Home)
    
    return render(request,"contact.html")

def About_blogs(request):
    return render(request,"about.html")


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)