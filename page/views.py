from django.shortcuts import render
from .models import Contant

# Create your views here.
def home(request):
    return render(request,'page/home.html')



def about(requset):
    return render(requset,'page/about.html')

def contact(requset):
    if requset.method == 'POST':
        v_name= requset.POST.get('name')
        v_email= requset.POST.get('email')
        v_subject= requset.POST.get('subject')
        v_massage= requset.POST.get('massage')


        v_contact=Contant(name=v_name,email=v_email,subject=v_subject,massage=v_massage)

        v_contact.save()
        return render(requset,'page/thank.html')


    else:
     return render(requset,'page/contact.html')



