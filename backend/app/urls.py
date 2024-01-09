from django.urls import path
from . import views

urlpatterns = [
    path('count/',views.CountView.as_view(),name='count'),
]
