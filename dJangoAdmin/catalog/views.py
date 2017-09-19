from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    wild_books = Book.objects.filter(title__contains='wild')
    number_wild_books = Book.objects.filter(title__contains='wild').count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                 'wild_books':wild_books,'number_wild_books':number_wild_books     },
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    
    context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'books/book_list.html'  # Specify your own template name/location
    paginate_by = 2
    
    def get_queryset(self):
        return Book.objects.all()
        #return Book.objects.filter(title__icontains='Ha')[:5] # Get 5 books containing the title war    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context    
    
    
      
class BookDetailView(generic.DetailView):
    model = Book    
    
    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
    
    
        #book_id=get_object_or_404(Book, pk=pk)
        
        return render(
            request,
            'catalog/book_detail.html',
            context={'book':book_id,}
        )