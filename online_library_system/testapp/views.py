from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm

# ========================
# Create Views (Add Data)
# ========================

def home(request):
    return render(request, 'testapp/home.html',)

def add_author(request):
    form = AuthorForm()
    if request.method=='POST':
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    return render(request, 'testapp/add_author.html', {'form': form})


def add_book(request):
    form = BookForm()
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'testapp/add_book.html', {'form': form})


def add_borrow_record(request):
    form =BorrowRecordForm()
    if request.method=='POST':
        form=BorrowRecordForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'testapp/add_borrow_record.html',{'form':form})




# ========================
# List Views (Paginated)
# ========================

def list_authors(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 10)  # 10 per page
    page = request.GET.get('page')
    authors_page = paginator.get_page(page)
    return render(request, 'testapp/list_authors.html', {'authors': authors_page})


def list_books(request):
    books = Book.objects.select_related('author').all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    books_page = paginator.get_page(page)
    return render(request, 'testapp/list_books.html', {'books': books_page})


def list_borrow_records(request):
    records = BorrowRecord.objects.select_related('book').all()
    paginator = Paginator(records, 10)
    page = request.GET.get('page')
    records_page = paginator.get_page(page)
    return render(request, 'testapp/list_borrow_records.html', {'records': records_page})


#
