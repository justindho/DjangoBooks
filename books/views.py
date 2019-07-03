from django.shortcuts import render, redirect
from .forms import CreateBookForm

from .models import Book

# Create your views here.
def create(request):
    """ Create a book to add to a user's book list. """
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            try:
                # Create Book object to store in db.
                book = Book()
                book.title = form.cleaned_data["title"]
                book.author = form.cleaned_data["author"]
                book.genre = form.cleaned_data["genre"]

                # Save the new Book object in the db.
                book.save()
                return redirect('')
            except:
                pass
        else:
            form = CreateBookForm()
        return render(request, 'books/create.html', {'form': form})
    else:
        form = CreateBookForm()
        return render(request, 'books/create.html', {'form': form})

def index(request):
    """ Show the user a his/her list of books. """
    reading_list = {
        "books": Book.objects.all()
    }
    return render(request, 'books/index.html', reading_list)

def update(request):
    """ Edit details of a user's book in their book list. """
    if request.method == 'POST':
        # Get updated book data from form
        book_selection = request.POST.get('book_selection')        
        book = Book.objects.get(id=book_selection)        
        new_title = request.POST.get('title')
        new_author = request.POST.get('author')
        new_genre = request.POST.get('genre')        

        # Update book information in database
        Book.objects.filter(title=book.title, author=book.author, genre=book.genre).update(title=new_title, author=new_author, genre=new_genre)         
        return redirect('index')
    else:
        books = Book.objects.all()
        return render(request, 'books/update.html', {'books': books})

def delete(request):
    """ Remove a book from a user's book list. """
    if request.method == 'POST':
        try:
            # Get array of books to remove.
            books = request.POST.getlist('checks[]')

            # Delete each book in array.
            for book in books:
                book = book.replace(' - ', ' ').split(' ')
                title, author, genre = book[0], book[1], book[2]
                Book.objects.filter(title=title, author=author,genre=genre).delete()
        except Exception as e:
            pass
        return redirect('index')
    else:
        # Get all books in reader's reading list.
        books = Book.objects.all()
        return render(request, "books/delete.html", {'books': books})