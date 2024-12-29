# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """Home page that displays all blog posts."""
    posts = BlogPost.objects.order_by('-date_added')  # Retrieve all posts in reverse chronological order
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

def check_post_owner(post, user):
    if post.owner != user:
        raise Http404
@login_required
def new_blog(request):
    """Add a new blog post."""
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)  # Create an instance without saving yet
            new_post.owner = request.user      # Assign the logged-in user as owner
            new_post.save()                    # Now save the post
            return redirect('blogs:index')     # Replace with your desired redirect
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_blog.html', {'form': form})

@login_required
def edit_blog(request, post_id):
    """Edit an existing blog post."""
    post = get_object_or_404(BlogPost, id=post_id)  # Get the blog post by ID
    # Make sure the topic belongs to the current user.
    check_post_owner(post, request.user)

    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)  # Pass the current post instance to the form
        if form.is_valid():
            form.save()
            return redirect('blogs:index')  # Redirect to the homepage after saving
    else:
        form = BlogPostForm(instance=post)  # Pre-fill the form with existing data
    return render(request, 'blogs/edit_blog.html', {'form': form, 'post': post})


# Delete view
@login_required
def delete_blog(request, post_id):
    """Delete a blog post."""
    post = get_object_or_404(BlogPost, id=post_id)  # Fetch the post by ID
    check_post_owner(post, request.user)
    post.delete()  # Delete the post
    return redirect('blogs:index')  # Redirect to the homepage (or the desired page)


# Details view
def detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogs/detail.html', {'post': post})