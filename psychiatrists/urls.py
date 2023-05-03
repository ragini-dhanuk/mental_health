from django.urls import path
from .import views

urlpatterns = [
   path('', views.all_psychiatrists, name='view_all'),
   path('<int:id>/view', views.view_psychiatrist, name="view")
]