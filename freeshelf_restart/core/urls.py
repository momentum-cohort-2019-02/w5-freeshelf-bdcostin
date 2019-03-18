from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<slug:slug>/', views.book_detail_view, name="book-detail"),
    path('author/<slug:slug>', views.author_detail_view, name="author-detail"),
]