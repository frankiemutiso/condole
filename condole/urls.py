from django.urls import path

from . import views

urlpatterns = [
    path('', views.deaths, name='deaths'),
    path('deaths/<int:pk>/', views.detail, name='detail'),
    path('deaths/<int:pk>/leave-message/',
         views.leave_message, name='leave-message'),
    path('condolences/', views.condolences, name='condolences'),
    path('create-death/', views.create_death, name='create-death')
]
