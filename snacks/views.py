from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime



class HomeView(TemplateView):
    template_name = "home.html"
   

class AboutView(TemplateView):
    template_name = "about.html"
