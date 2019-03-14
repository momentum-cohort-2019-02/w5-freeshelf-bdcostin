from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<slug:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
