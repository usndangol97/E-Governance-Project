from django.shortcuts import render
from .forms import Form1, Form2
from .models import PersonalDetail, AddressDetail

# Create your views here.
# index function returns a home page.
def index(request):
    context={}
    return render(request,'core/index.html',context)

#FormView method takes in two forms and renders it on views
def FormView(request):
    if request.method == 'POST':
        form = Form1(request.POST, prefix='formA')
        form2 = Form2(request.POST, prefix='formB')
        if form.is_valid() and form2.is_valid():
            p_form=form.save()

            form2.cleaned_data["p_form"]=p_form
            a_form=form2.save()
            a_form.p_form=p_form
            a_form.save()
    else:
        form = Form1(prefix='formA')
        form2 = Form2(prefix='formB')

    context = {'form':form, 'form2':form2}
    return render(request, "core/license_registration.html", context)

#Delivers data from database into html page
def Result(request):
    info = PersonalDetail.objects.all().order_by('-id')[:1]
    addr = AddressDetail.objects.all().order_by('-id')[:1]
    
    context = {
        'info':info,
        'addr':addr,
    }
    return render(request,'core/reg_pdf.html',context)