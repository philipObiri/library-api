from django.urls import path 
from .views import BooksListAPIView

urlpatterns = [
    path("",BooksListAPIView.as_view(),name="book_list" ),
]
