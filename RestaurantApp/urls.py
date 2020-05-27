
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index , name="index"),
    path('contactUs' , views.contactUs , name="contactUs"),
    path('aboutUs' , views.aboutUs , name="aboutUs"),
]
