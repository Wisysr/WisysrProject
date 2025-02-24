from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='other_index')
]