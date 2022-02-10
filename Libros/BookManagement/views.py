from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookForm
# Create your views here.


def bookCreate(request):
    bookForm = BookForm()
    return render(request, "BookManagement/bookCreate.html", {
        "bookForm": bookForm
    })

def bookRead(request):
    return

def bookUpdate(request):
    return

def bookDelete(request):
    return