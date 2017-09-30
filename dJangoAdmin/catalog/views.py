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
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                 'wild_books':wild_books,'number_wild_books':number_wild_books,
                 'num_visits':num_visits},
    )


from django.contrib.auth.models import User
import pyodbc 
import pandas.io.sql as sql
from django import forms
import datetime   
from .forms import NameForm
from .forms import PeriodFilter
from datetime import date


 
def dashboard(request):
 
    user = User.objects.get(id=2)
    user_email = user.email

    from_date = 1234

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PeriodFilter(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            (from_date, to_date) = form.cleaned_data['Range']

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PeriodFilter(initial={'range': (date.today(), date.today())})

    
    
    


#    server = '10.203.1.105\\alpha' 
#    database = 'test_yang' 
#    username = 'webuser' 
#    password = 'Changeme1' 
#    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#    cursor = cnxn.cursor()
#
#    query = """
#    select Count(*) Router 
#    from AEPerformanceReport_1 as a 
#    inner join topDownAELookupTable as b 
#    on a.Date >= (select lastlastSaturday from DataDrivenReport_DateRange)
#    and a.Date <= (select lastFriday from DataDrivenReport_DateRange)
#    and a.PersonID = b.PersonId 
#    and b.Email = 'aaa@aaa.com'
#    and EventName = 'Router Call'
#    """
# 
#
#    query = query.replace('aaa@aaa.com',user_email)
#   
#    queryResult = sql.read_sql(query, cnxn)
    
#    num_Router_lstWk = queryResult["Router"][0]

    num_Router_lstWk=from_date
    template_name = 'GDashboard/production/index.html'
    return render(
        request, 
        'GDashboard/production/index.html',
        context={'num_leads_yst':num_Router_lstWk,'user_email':user_email,'form':form},
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


class AuthorListView(generic.ListView):
    model = Author
    
    context_object_name = 'author_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'authors/author_list.html'  # Specify your own template name/location
    paginate_by = 2
    
    def get_queryset(self):
        return Author.objects.all()
        #return Book.objects.filter(title__icontains='Ha')[:5] # Get 5 books containing the title war    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context    
    

      
class AuthorDetailView(generic.DetailView):
    model = Author    
    
    def author_detail_view(request,pk):
        try:
            author_id=Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404("Book does not exist")  
        #book_id=get_object_or_404(Book, pk=pk)
        
        return render(
            request,
            'catalog/author_detail.html',
            context={'author':author_id,}
        )


        
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')



from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import RenewBookForm

def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
  


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_death':'12/10/2016',}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

        