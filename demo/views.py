from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.

class Another(View):

    books = Book.objects.get(id=2)
    output = ''
    get_method_output = f"We have {books.title} book with ID {books.id}<br>"

    #for book in books:

        #output += f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.get_method_output)


def first(request):
    return HttpResponse('First message from views!')
