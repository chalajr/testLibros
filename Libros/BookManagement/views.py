from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BookForm
from .models import *
# Create your views here.


def bookCreate(request):
    #Revisamos el metodo de entrada
    if request.method == "POST":
        #Creamos una variable con el formulario y la informacion que envio el usuario
        bookFormRequest = BookForm(request.POST)
        #Validamos el formulario
        if bookFormRequest.is_valid():
            #Guardamos la nueva entidad en la base de datos
            bookFormRequest.save()
        #Redireccionamos al usuario
        return redirect('BookManagement:bookCreate')
    else:
        bookForm = BookForm()
        bookList = Book.objects.all()
        return render(request, "BookManagement/bookCreate.html", {
            "bookForm": bookForm,
            "bookList": bookList
        })

def bookRead(request):
    return

def bookUpdate(request):
    return

def bookDelete(request):
    return

    