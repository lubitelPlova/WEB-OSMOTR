from django.urls import path
# from web_osmotr.urls import urlpatterns
from .views import HomePageView, DoctorsListView, PatientsListView

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('patients', PatientsListView.as_view(), name='patients'),
    path('doctors', DoctorsListView.as_view(), name='doctors')
]