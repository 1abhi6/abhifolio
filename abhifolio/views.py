from django.shortcuts import render
from header.models import header_model
# Home page


def home(request):
    header_model_data = header_model.objects.all()[:1]
    return render(request, 'index.html', {'header_model_data': header_model_data})
