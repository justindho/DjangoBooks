from django.shortcuts import render, redirect
from .forms import BookForm

from .models import Book

# Create your views here.
def create(request):
    """ Create a book to add to a user's book list. """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                # Create Book object to store in db.
                book = Book()
                book.title = form.cleaned_data["title"]
                book.author = form.cleaned_data["author"]
                book.genre = form.cleaned_data["genre"]

                print('book title: ' + book.title)

                # Save the new Book object in the db.
                book.save()
                return redirect('')
            except:
                pass
        else:
            form = BookForm()
        return render(request, 'books/create.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'books/create.html', {'form': form})

def index(request):
    """ Show the user a his/her list of books. """    
    context = {
        "books": Book.objects.all()
    }    
    return render(request, 'books/index.html', context)

# def update(request, id):
#     """ Edit details of a user's book in their book list. """
#     book = Book.objects.get(id=id)
#     return render(request, 'templates/edit.html', {'book': book})

# def delete(request, id):
#     """ Remove a book from a user's book list. """
#     book = Book.objects.get(id=id)
#     book.delete()
#     return redirect('')