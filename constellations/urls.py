from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('courses/', views.courses, name='courses'),
    path('mailing_list/', views.mailing_list, name='mailing-list'),
    path('testimonials/', views.student_testimonials.as_view(), name='testimonials')
]
