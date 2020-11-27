from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.

def first(request):
    return render(request, 'first_temp.html', {'data': 'This is data from views'})

# class Another(View):
#
#     books = Book.objects.get(id=1)
#     output = ''
#     get_method_output = f"We have {books.title} book with ID {books.id}<br>"
#
#     for book in books:
#         output += f"We have {book.title} book with ID {book.id}<br>"
#
#     def get(self, request):
#         return HttpResponse(self.get_method_output)



