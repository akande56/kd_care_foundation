from django.shortcuts import render
from django.http import request
from django.views.generic import TemplateView
# Create your views here.


# def home():

#     return render(request, 'index.html', {"message": "hello"})


class home(TemplateView):
    template_name = "index.html"

class about(TemplateView):
    template_name = "about-us.html"

class contact(TemplateView):
    template_name = "contacts.html"
