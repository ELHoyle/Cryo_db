from django.urls import path
from . import views

urlpatterns = [
    #ex: /sample_management/
    path('', views.index, name ='index'),
    #ex: /sample_management/99-99999
    path('<int:hp_accession>/', views.detail, name ='detail')

]