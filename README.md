## DjangoBooks
DjangoBooks allows users to keep track of a list of books that they've been wanting to read but just have not had the time to do so yet. Users can create an account and login to view their reading list. Users can also filter their reading list to view books by author or genre. 

This project uses Django's default object-relational mapping layer (ORM) to query the database for a user's reading list and associated operations on it.

### Screenshots
![](/images/booklist.png)
![](/images/booklist_filtered.png)
![](/images/add_book.png)
![](/images/remove_books.png)
![](/images/update_book.png)

### Installing
1. Open a command line interface.
2. Change the current working directory to the location where you want the cloned directory to be made.
3. Type `git clone https://github.com/justindho/DjangoBooks` and press <b>Enter</b>
4. Run `pip install -r requirements.txt` in your shell. 

### Run the Project
1. In the project's root directory, create a file called `secret_settings.py`.
2. In `secret_settings.py`, set `SECRET_KEY = "ENTER YOUR SECRET KEY HERE"` to be any string containing a mixture of numbers, letters, and symbols.
1. Change the current working directory to the project's root directory where `manage.py` is located.
2. Run `python manage.py runserver` in your shell.
3. Click on the link in your shell (http://127.0.0.1:8000/) and you will be taken to DjangoBooks, where you can create an account and login to start creating your reading list!

### Built With
- Python - The backend language used
- Django - The web framework used
- Javascript - Used to update the user's reading list via AJAX when filtering by author/genre
- HTML - Used to render page templates
- Bootstrap - Used to make the UI nicer

### What I Learned
- How to create an application with Django
