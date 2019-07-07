from django.urls import path

from . import views

# app_name = "books"
urlpatterns = [
    # path("<int:user_id>", views.index, name="index"),
    # path("<int:user_id>/create/", views.create, name="create"),
    # path("<int:user_id>/delete/", views.delete, name="delete"),
    # path("<int:user_id>/update/", views.update, name="update"),
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/", views.delete, name="delete"),
    path("update/", views.update, name="update"),
    path("query/", views.query_filter, name="query"),
]
