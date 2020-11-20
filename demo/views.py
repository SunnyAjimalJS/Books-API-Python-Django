from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.

class Another(View):

    books = Book.objects.filter(is_published=True)
    output = ''

    for book in books:

        output += f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views!')
