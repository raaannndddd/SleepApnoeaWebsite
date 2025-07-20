from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('result/', views.result_view, name='result'),
    path('loading/', views.loading, name='loading'),
    path('upload/', views.upload_audio, name='upload'),
    path('choose/', views.choose_input_method, name='choose'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]