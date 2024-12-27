from django.urls import path
from . import views  # Import views from the current app

app_name = 'learning_logs'

urlpatterns = [
    path('', views.home, name='index'),  # Home page URL
    path('topics/', views.topics, name='topics'),  # Topic page URL
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'), 
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edi_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
