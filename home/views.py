from django.shortcuts import render
from .models import Customercustomerdemo
from .models import Categories
# Create your views here.


def home(request):
    data = Categories.objects.all().values()
    # data = Customercustomerdemo.objects.all().values()
    return render(request,'home/home.html',locals())
