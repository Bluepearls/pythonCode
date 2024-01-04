from django.http import HttpResponse
def hello():
    return HttpResponse("Hello, World!")

hello()