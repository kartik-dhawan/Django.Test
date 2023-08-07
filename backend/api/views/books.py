from django.http import JsonResponse
from books.models import Book
from django.forms.models import model_to_dict
import json

# Create your views here.


def get_all_books(request, *args, **kwargs):
    print(request.GET)

    all_books = Book.objects.all()
    first_book = Book.objects.all().first()
    len = int(model_to_dict(Book.objects.all().last())['id'])
    print('len')
    print(len)

    data = {}
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # data['method'] = request.method
    # data['results'] = [{"name": "kartik"}]
    # data['params'] = dict(request.GET)
    # data['body'] = dict(json.loads(request.body))

    if all_books:
        global res
        # res = model_to_dict()
        res = all_books

    return JsonResponse(model_to_dict(first_book))
