from django.http import JsonResponse

# Create your views here.


def get_all_books(request, *args, **kwargs):
    return JsonResponse({"name": "Kartik"})
