from django.shortcuts import render
from django.http import HttpResponse
from .models import joker
# Create your views here.

def index(request):
    if request.method == 'POST' :
        fname= request.POST['fname']
        may=joker(name=fname)
        may.save()
        return HttpResponse('ok')
    else:
        return render(request,'index.html')