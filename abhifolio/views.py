from django.http import HttpResponse

# Home page
def home(request):
    return HttpResponse("Hello")

    