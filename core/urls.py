
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('jobs/', views.InternshipListView.as_view(), name='internship-list'),
    path('apply/', views.ApplicationCreateView.as_view(), name='apply'),
    path('edit/<int:pk>/', views.ApplicationUpdateView.as_view(), name='app-update'),
]
