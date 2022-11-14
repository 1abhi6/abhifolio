from django.shortcuts import render
from header.models import header_model
from about.models import about_model
from meta_header.models import meta_header_model
from service.models import service_model
from myportfolio.models import myportfolio_model
from skill.models import skill_model

# Home page


def home(request):
    header_model_data = header_model.objects.all()[:1]
    about_model_data = about_model.objects.all()[:1]
    service_model_data = service_model.objects.all()
    myportfolio_model_data = myportfolio_model.objects.all()
    skill_model_data = skill_model.objects.all()
    data = {
        'header_model_data': header_model_data,
        'about_model_data': about_model_data,
        'service_model_data': service_model_data,
        'myportfolio_model_data': myportfolio_model_data,
        'skill_model_data': skill_model_data
    }
    return render(request, 'index.html', data)
