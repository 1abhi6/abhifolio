from django.shortcuts import render
from header.models import header_model
from about.models import about_model
from meta_header.models import meta_header_model
from service.models import service_model
from myportfolio.models import myportfolio_model
from skill.models import skill_model
from contact.models import contact_model
from django.core.mail import send_mail, EmailMultiAlternatives
# Home page


def home(request):
    header_model_data = header_model.objects.all()[:1]
    about_model_data = about_model.objects.all()[:1]
    service_model_data = service_model.objects.all()
    myportfolio_model_data = myportfolio_model.objects.all()
    skill_model_data = skill_model.objects.all()

    # Contact
    submitted = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        save_data = contact_model(
            name=name, email=email, subject=subject, message=message)
        save_data.save()
        submitted = True
    data = {
        'header_model_data': header_model_data,
        'about_model_data': about_model_data,
        'service_model_data': service_model_data,
        'myportfolio_model_data': myportfolio_model_data,
        'skill_model_data': skill_model_data,
        'submitted': submitted
    }
    return render(request, 'index.html', data)


# def contact(request):
#     submitted = False
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         save_data = contact_model(
#             name=name, email=email, subject=subject, message=message)
#         save_data.save()
#         submitted = True

#         # Sending email to myself about someone has registered
#         # email_subject = "New enquiry from Contact page: {}".format(subject)
#         # from_email = '1abhigup6@gmail.com'
#         # to_email = 'abhishekguptacode@gmail.com'
#         # email_message = '''
#         #     New Enquiry: <br>
#         #     Name: {} <br> Email: {} <br> Subject: {} <br> Message: {}
#         #     '''.format(name, email, subject, message)
#         # send_mail_to_me = EmailMultiAlternatives(
#         #     email_subject, email_message, from_email, [to_email])
#         # send_mail_to_me.content_subtype = 'html'
#         # send_mail_to_me.send()
#     data = {
#         'submitted': submitted
#     }
#     return render(request, 'contact.html', data)
