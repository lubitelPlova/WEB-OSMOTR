from django.urls import path

# from web_osmotr.urls import urlpatterns
from .views import HomePageView

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home')
]