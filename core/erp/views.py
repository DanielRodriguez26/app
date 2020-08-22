from django.http import HttpResponse
from django.shortcuts import render
from core.erp.models import Category, Product



def myfirstview(request):
  data = {
    'name' : 'Daniel',
    'categories' : Category.objects.all()

  }
  return render(request, 'home.html', data)

def mysecondview(request):
  data = {
    'name' : 'Daniel',
    'products' : Product.objects.all()

  }
  return render(request, 'second.html', data)