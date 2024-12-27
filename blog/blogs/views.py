# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """Home page that displays all blog posts."""
    posts = BlogPost.objects.order_by('-date_added')  # Retrieve all posts in reverse chronological order
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def new_blog(request):
    """Add a new blog post."""
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')  # Redirect to the homepage
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_blog.html', {'form': form})

def edit_blog(request, post_id):
    """Edit an existing blog post."""
    post = get_object_or_404(BlogPost, id=post_id)  # Get the blog post by ID
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)  # Pass the current post instance to the form
        if form.is_valid():
            form.save()
            return redirect('blogs:index')  # Redirect to the homepage after saving
    else:
        form = BlogPostForm(instance=post)  # Pre-fill the form with existing data
    return render(request, 'blogs/edit_blog.html', {'form': form, 'post': post})


# Delete view
def delete_blog(request, post_id):
    """Delete a blog post."""
    post = get_object_or_404(BlogPost, id=post_id)  # Fetch the post by ID
    post.delete()  # Delete the post
    return redirect('blogs:index')  # Redirect to the homepage (or the desired page)
