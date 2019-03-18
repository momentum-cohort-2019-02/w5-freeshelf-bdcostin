from django.urls import path, include
from shelf.views import BookDetailView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shelf/', views.index, name='index'),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<slug:pk>', views.AuthorDetailView.as_view(), name='author-details'),
]

