from django.shortcuts import render
from header.models import header_model
from about.models import about_model
from meta_header.models import meta_header_model

# Home page


def home(request):
    header_model_data = header_model.objects.all()[:1]
    about_model_Data = about_model.objects.all()[:1]
    data = {
        'header_model_data': header_model_data,
        'about_model_Data': about_model_Data
    }
    return render(request, 'index.html', data)


