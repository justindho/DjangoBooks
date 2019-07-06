# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def index(request):
#     if not request.user.is_authenticated:
#         return render(request, "users/login.html", {"message": None})
#     context = {
#         "user": request.user
#     }
#     return render(request, "users/user.html", context)

# def login_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "users/login.html", {"message": "Invalid credentials."})

# def logout_view(request):
#     logout(request)
#     return render(request, "users/login.html", {"message": "User logged out."})

# def register_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#     else:
#         return render(request, "users/register.html")