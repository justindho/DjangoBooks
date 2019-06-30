from django.shortcuts import render, redirect
from .forms import BookForm

from .models import Book

# Create your views here.
# def create_book(request):
#     """ Create a book to add to a user's book list. """
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#         else:
#             form = BookForm()
#         return render(request, 'templates/create.html', {'form': form})

def index(request):
    """ Show the user a his/her list of books. """
    context = {
        "books": Book.objects.all()
    }    
    return render(request, 'books/index.html', context)

# def edit_book(request, id):
#     """ Edit details of a user's book in their book list. """
#     book = Book.objects.get(id=id)
#     return render(request, 'templates/edit.html', {'book': book})

# def delete_book(request, id):
#     """ Remove a book from a user's book list. """
#     book = Book.objects.get(id=id)
#     book.delete()
#     return redirect('/')