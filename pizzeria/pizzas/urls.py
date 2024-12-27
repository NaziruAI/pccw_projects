from django.urls import path
from . import views  # Import views from the current app

app_name = 'pizzas'

urlpatterns = [
    path('', views.home, name='index'),  # Home page URL
    path('pizzas/', views.pizzas, name='pizzas'),  # Topic page URL
    # Detail page for a single topic
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'), 
    # Page for editing an entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
