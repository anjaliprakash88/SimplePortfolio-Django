from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exp', views.experience, name='exp'),
    path('skills', views.skills, name='skills'),
    path('contact', views.contact, name='contact'),
]