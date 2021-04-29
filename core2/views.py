from django.shortcuts import render, redirect
from django.views.generic import View
from .render import Render
from .forms import ResumeForm
from .models import Resume
# Create your views here.

def CvCreate(request):
    form = ResumeForm(request.POST or None)

    if form.is_valid():
        form.save() 
        return redirect('../create')    

    # fields = ('name','birthdate','father','mother')  
    model = Resume  
    context = {
        'form':form
    }     

    return render(request,'core2/create.html',context)

class Pdf(View):
    def get(self, request):
        info = Resume.objects.all().order_by('-id')[:1]
        params = {
            'info': info,
            'request': request
        }
        return Render.render('core2/pdf.html', params)