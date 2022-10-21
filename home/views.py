from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("This is our home page")
    context = {'variable1': 'Harry is great',
               'variable2': 'Jesvika is great'
               }

    return render(request, "index.html", context)


def aboutus(request):
    return render(request, "about.html")
    # return HttpResponse("This is our about page")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        destination = request.POST.get('destination')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, mobile=mobile, message=message, destination=destination,
                          date=datetime.today())
        contact.save()
        messages.success(request, 'Your request is recieved.Our team will contact you soon!')
    # else:
    #     messages.error(request, 'Something went wrong!!!Please try after some time.')

    return render(request, "contact.html")


def tours(request):
    return render(request, "tours.html")

def booknow(request):
    return render(request,"booknow.html")

