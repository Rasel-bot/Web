from django.shortcuts import render, HttpResponse
from datetime import datetime
from window.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context ={"power":"more active than before",
              "life": "remaining 3"
    }
    return render(request, "index.html", context)
    
def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Submitted message succesfully.")
    return render(request,"contact.html")

def erp(request):
    return render(request,"erp.html")

