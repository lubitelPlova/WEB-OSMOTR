from django.urls import path
# from web_osmotr.urls import urlpatterns
from .views import HomePageView, DoctorsListView, PatientsListView, ExaminationsList, ExaminationDetailView, SearchView

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('patients', PatientsListView.as_view(), name='patients'),
    path('doctors', DoctorsListView.as_view(), name='doctors'),
    path('examinations', ExaminationsList.as_view(), name='examination'),
    path('examinations/<int:pk>', ExaminationDetailView.as_view(), name='examination_detail'),
    path('search', SearchView.as_view(), name='search')
]