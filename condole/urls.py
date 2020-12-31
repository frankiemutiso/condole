from django.urls import path

from . import views

urlpatterns = [
    path('', views.deaths, name='deaths'),
    # path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/leave-message/',
         views.leave_message, name='leave-message'),
    path('create-death/', views.create_death, name='create-death')
]
