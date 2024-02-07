from django.urls import path     
from . import views

urlpatterns = [
    path('', views.add_book),   
    path('author/<int:author_id>', views.show_author),  
]