from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    # path("create/", views.create_book),
    # path("delete/", views.delete_book),
    # path("edit/", views.edit_book),
]
