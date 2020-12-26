from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_message, name='post-message'),
    path('condolences/', views.condolences, name='condolences'),
    path('deaths/', views.deaths, name='deaths'),
    path('create-death/', views.create_death, name='create-death')
]
