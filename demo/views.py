from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.

class Another(View):

    books = Book.objects.all()

    output = f"We have {len(books)} that many books in DB"

    def get(self, request):
        return HttpResponse('This is another function inside a class')


def first(request):
    return HttpResponse('First message from views!')
