from django.http import JsonResponse, HttpResponse
from django.core import serializers
from books.models import Book
from django.forms.models import model_to_dict
import json

# Create your views here.


def get_all_books(request, *args, **kwargs):
    # print(request.GET)

    data = {}
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # data['method'] = request.method
    # data['results'] = [{"name": "kartik"}]
    # data['params'] = dict(request.GET)
    # data['body'] = dict(json.loads(request.body))

    all_books = Book.objects.all()
    books_list = serializers.serialize('json', all_books)

    # print(books_list)

    return JsonResponse(json.loads(books_list), safe=False)
