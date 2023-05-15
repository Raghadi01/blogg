
from django.shortcuts import render

def baby(requset):
    return render(requset,'Gallery/baby.html')


def country(requset):
    return render(requset, 'Gallery/country.html')


def product(requset):
    return render(requset, 'Gallery/product.html')




# Create your views here.
