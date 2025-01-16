from django.shortcuts import render

# Create your views here.
from django.views. generic import TemplateView
# https://wguide.rw/tablica-osnovnykh-tegov-html-s-primerami
from django. shortcuts import render

def index (request):
    return render(request, ' templates/second_task/func_template.html')

class index2 (TemplateView):
    template_name = ' templates/second_task/class_template.html'