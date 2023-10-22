from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('firstp/', views.first, name='members'),
    path('addDetails/',views.AddDetails),
    path('addDetails/showall/',views.ShowDetails),
]