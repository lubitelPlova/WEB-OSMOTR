from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from shop.models import Patient, Doctor
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class PatientsListView(ListView):
    template_name = 'patients.html'
    model = Patient
    context_object_name = 'list_of_all_patients'

class DoctorsListView(ListView):
    template_name = 'doctor.html'
    model = Doctor
    context_object_name = 'list_of_all_doctors'