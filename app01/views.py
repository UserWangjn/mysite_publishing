from django.shortcuts import render,HttpResponse
from app01.models import Publishing

# Create your views here.

def publishing_list(req):
    ret = Publishing.objects.all()
    print(ret)

    return render(req,'publishing_list.html',{'ret':ret})