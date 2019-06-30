from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    # path("delete/", views.delete, name="delete"),
    # path("update/", views.update, name="update"),
]
