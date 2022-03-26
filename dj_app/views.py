from django.shortcuts import render,HttpResponse
from dj_app.models import Contact
# Create your views here.
def index(request) :
    return render(request,'index.html')

def about(request) :
    return render(request,'about.html')

def contact(request) :
        if request.method == 'POST':
            contact = Contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact.name=name
            contact.email=email
            contact.message=message
            contact.save()
           
            return HttpResponse('<h1>Thanks for Contact with us</h1>')

        return render(request,'contact.html')

def Show_data(request) :
    data=Contact.objects.all()
    for i in data:
        print (i)
    return render(request,'data.html',{'Contact':data}) 

def project(request) :
    return render(request,'project.html')