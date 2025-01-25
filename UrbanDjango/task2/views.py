from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views. generic import TemplateView
# https://wguide.rw/tablica-osnovnykh-tegov-html-s-primerami
from django. shortcuts import render
products = [
{"name": "Смартфон", "price": 15000},
{"name": "Ноутбук", "price": 55000},
{"name": "Планшет", "price": 25000},
]

def product_list(request):
    product_items = "<br>".join([f"{p['name']}: {p['price']} руб." for p in products])
    #return HttpResponse(product_items)
    return render(request, 'product_list.html', {'product_items': product_items})

def index (request):
    return ( render(request, 'func_template.html'))

class index2 (TemplateView):
    template_name = 'class_template.html'


