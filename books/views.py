from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateBookForm

from .models import Book
from users.models import CustomUser

# Create your views here.
@login_required
def create(request):
    """ Create a book to add to a user's book list. """
    if request.method == 'POST':        
        form = CreateBookForm(request.POST)
        if form.is_valid():
            try:
                # Check if book is already in user's reading list.
                title = form.cleaned_data["title"]
                author = form.cleaned_data["author"]
                genre = form.cleaned_data["genre"]
                duplicate_count = Book.objects.filter(title=title, author=author, genre=genre).count()
                
                if duplicate_count > 0:
                    return redirect('index')
                
                # Create Book object to store in db.
                book = Book()
                book.title = form.cleaned_data["title"]
                book.author = form.cleaned_data["author"]
                book.genre = form.cleaned_data["genre"]
                # book.user = str(request.user)
                book.user = request.user
                
                # Save the new Book object in the db.
                book.save()                
                return redirect('index')
            except Exception as e:
                print(e)
                pass
        else:
            print('form is not valid')
            form = CreateBookForm()
        return render(request, 'books/create.html', {'form': form})
    else:
        form = CreateBookForm()
        return render(request, 'books/create.html', {'form': form})

@login_required
def index(request):
    """ Show the user his/her list of books. """
    # Query for author and genre filters
    # if request.method == 'POST':
    #     form =
    
    user = request.user
    username = CustomUser.objects.get(username=user.username)    

    context = {
        "authors": list(Book.objects.order_by('author').values_list('author', flat=True).distinct()),        
        "books": Book.objects.filter(user=username),
        "genres": list(Book.objects.order_by().values_list('genre', flat=True).distinct()),
        "user": str(user)
    }
    return render(request, 'books/index.html', context)

@login_required
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

@login_required
def delete(request):
    """ Remove a book from a user's book list. """
    if request.method == 'POST':
        try:
            # Get array of books to remove.
            books = request.POST.getlist('checks[]')
            print(books)

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

@login_required
def book_details(request):
    """ View more information about a book. """
    pass

    # Show number of pages
    # Show current price on several different websites