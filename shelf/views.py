from django.shortcuts import render, get_object_or_404, redirect
from shelf.models import Author, Book, Topic
from django.views import generic
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
    return render(request, 'shelf/index.html', context=context)

class BookDetailView(generic.DetailView):
    model = Book
    slug_field = 'Book.title'
    slug_url_kwarg = 'Book.title'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['books'] = Book.objects.all()
        return context

    def book_detail_view(self, request, slug):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'shelf/book_detail.html', {'book': book})

# class BookListView(generic.ListView):
#     model = Book

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(BookListView, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context

class BookListView(generic.ListView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class TopicListView(generic.ListView):
    model = Topic
