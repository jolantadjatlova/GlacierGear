from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('terms/', views.terms, name='terms'),
]
