from django.urls import path
from . import views

urlpatterns = [    
    path('', views.add_client, name='add_client'),
    path('<int:id>', views.view_client, name='view_client'),
    path('all/', views.all_clients, name='all_client')
]