from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('doctor/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('contact/', views.contact, name='contact'),
    path('confirmation/', views.confirmation, name='confirmation'),
]