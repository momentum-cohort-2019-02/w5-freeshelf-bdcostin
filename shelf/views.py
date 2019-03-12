from django.shortcuts import render
from shelf.models import Author, Book, Topic
from django.views import generic
# Create your views here.

def index(request):
    '''View function for home page of site.'''

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class TopicListView(generic.ListView):
    model = Topic
