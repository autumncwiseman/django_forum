from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .form import PostForm


def index (request):
    # If thee method is POST
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
    # If the form is valid
        if form.is_valid():
        # Yes, Save
            form.save()
        
        # Redirect to Home
            return HttpResponseRedirect('/')
        else: 
        # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

        # Get all post, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

        # Show
    return render(request, 'posts.html',
                      {'posts': posts})

def delete(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')



