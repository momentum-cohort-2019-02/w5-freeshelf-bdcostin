from django.shortcuts import render, get_object_or_404, redirect
from shelf.models import Author, Book, Topic
from django.views import generic
# Create your views here.

def index_view(request):
    '''View function for home page of site.'''

    topics = Topic.objects.all()
    books = Book.objects.all()

    context = {
        'topics': topics,
        'books': books,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'shelf/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    def book_detail_view(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        return render(request, 'shelf/book_detail.html', {'book': book})

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class TopicListView(generic.ListView):
    model = Topic
