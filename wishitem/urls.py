from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishitem, name='view_wishitem')
]