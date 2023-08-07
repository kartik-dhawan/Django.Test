from django.http import JsonResponse
import json

# Create your views here.


def get_all_books(request, *args, **kwargs):
    print(request.GET)

    data = {}
    # data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['method'] = request.method
    data['results'] = [{"name": "kartik"}]
    data['params'] = dict(request.GET)
    data['body'] = dict(json.loads(request.body))
    return JsonResponse(data)
