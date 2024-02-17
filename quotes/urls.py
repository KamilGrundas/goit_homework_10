from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.quotes_list, name='quotes_list'),
    path('register/', views.register, name='register'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
