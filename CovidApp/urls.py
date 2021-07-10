from django.urls import path
from . import views

urlpatterns = [

    path('CovidApp/', views.index) # our-domain.com/CovidApp/


]