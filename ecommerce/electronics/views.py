from django.shortcuts import render
from django.http import HttpResponse
from .forms import ElectronicsRegistration
from electronics.models import  Student
from django.http import HttpResponseRedirect
from . models import Info


def blog(request):
    return render(request, 'electronics/forms1.html')


def student_info(request):
    sdetails = Student.objects.all() # Show all query sets
    return render(request,'electronics/std.html', {'std': sdetails} )


def show_form(request):
    if request.method == 'POST':
        frm = ElectronicsRegistration(request.POST)
        if frm.is_valid():
            print('Valied form')
            fname = frm.cleaned_data['first_name']
            lname = frm.cleaned_data['last_name']
            email = frm.cleaned_data['email']
            bth =frm.cleaned_data['batch']
            pas = frm.cleaned_data['password']
            rpas =frm.cleaned_data['re_password']
            txt =frm.cleaned_data['textarea']
            roll = frm.cleaned_data['rollno']
            pay = frm.cleaned_data['payment']
            dj =frm.cleaned_data['django']
            djangoone = Info(first_name=fname, last_name = lname, email=email, batch=bth, password =pas, re_password =rpas, textarea=txt, rollno =roll, payment=pay, django=dj )

            djangoone.save()

            return HttpResponseRedirect('/successfully/')
    
    else:
        frm = ElectronicsRegistration(auto_id='emp_%s', label_suffix='', initial={'email': 'shorif@gmail.com'})
       # frm.order_fields(field_order=['email',  'rollno', 'last_name' , 'first_name' ,   'batch' ])
        print("Execute GET")    
    return render (request, 'electronics/forms.html', {'form': frm})


def success(request):
    return render(request, 'electronics/submit.html')
        


