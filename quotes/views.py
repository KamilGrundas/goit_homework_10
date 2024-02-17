from django.shortcuts import render, redirect
from .models import Quote, Tag, Author
from django.contrib.auth import authenticate, login
from .forms import QuoteForm, MyUserCreationForm, AuthenticationForm
from django.contrib.auth import login



def quotes_list(request):
    quotes = Quote.objects.all()
    
    authors = Author.objects.all()
    tags = Tag.objects.all()
    context = {"quotes" : quotes,
               "authors" : authors,
               "tags" : tags}
    return render(request, "quotes/quotes_list.html", context)



def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = MyUserCreationForm()
    return render(request, 'quotes/register.html', {'form': form})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            form.save_m2m()
            return redirect("/")
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                print("błąd")
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'quotes/login.html', {'form': form})