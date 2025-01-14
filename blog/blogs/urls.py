"""Defines URL patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	path('new_blog/', views.new_blog, name='new_blog'),
	path('edit_blog/<int:post_id>/', views.edit_blog, name='edit_blog'),
	path('delete_blog/<int:post_id>/', views.delete_blog, name='delete_blog'), 
    path('blogs/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    
]