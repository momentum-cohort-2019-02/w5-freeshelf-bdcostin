from django.shortcuts import render, get_object_or_404
from core.models import Author, Book, Topic
# from django.core.paginator import Paginator

# Create your views here.

def index(request):
    '''View function for home page of site.'''

    topics = Topic.objects.all()
    books = Book.objects.all()
    authors = Author.objects.all()

    context = {
        'books': books,
        'topics': topics,
        'authors': authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def book_detail_view(request, slug):
    '''Book detail page to show info for specific ebook'''
    books = get_object_or_404(Book, slug=slug)
    topics = Topic.objects.all()
    return render(request, "book-detail.html", {
        'books': books,
        'topics': topics,
        })

def author_detail_view(request, slug):
    '''Author detail page to show info for specific ebook'''
    authors = get_object_or_404(Author, slug=slug)
    books = Book.objects.all()
    return render(request, "book-detail.html", {
        'books': books,
        'authors': authors,
        })

