from django.urls import path
from . import views
from .views import nmap_scan

urlpatterns =[
    path('nmap-scan/<str:ip_address>/', nmap_scan, name='nmap_scan'),
    path('run-command/', views.run_command, name='run_command'),

]