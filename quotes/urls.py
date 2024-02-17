from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.quotes_list, name="quotes_list"),
    path("register/", views.register, name="register"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("create_author/", views.create_author, name="create_author"),
    path("load_authors/", views.load_authors, name="load_authors"),
    path("load_quotes/", views.load_quotes, name="load_quotes"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
]
