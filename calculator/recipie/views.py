from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def calculate(request):
    response = {
        request.GET['recipe']
    }

    return HttpResponse(response)
