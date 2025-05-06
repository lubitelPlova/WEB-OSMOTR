from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView
from shop.models import Patient, Doctor, MedicalExamination
from django.db.models import Q


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

class ExaminationsList(ListView):
    template_name = 'examinations.html'
    model = MedicalExamination
    context_object_name = 'list_of_all_examinations'

class ExaminationDetailView(DetailView):
    template_name = 'examination_detail.html'
    model = MedicalExamination
    context_object_name = "examination"

class SearchView(ListView):
    template_name = 'search.html'
    model = MedicalExamination
    context_object_name = 'list_of_all_examinations'

    def get_queryset(self):
        query = self.request.GET.get('q')

        return MedicalExamination.objects.filter(
            Q(patient_id__name__icontains=query) #  |
            # Q(doctor_id__name__icontains=query)
            ).order_by('datetime').reverse()