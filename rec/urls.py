from django.urls import path, include

from django.contrib.auth import views as auth_views # "as auth_views" para serparar das views originais

from .views import ConvenioListView, ConvenioDetailView, ConvenioCreateView, ConvenioUpdateView, ConvenioDeleteView

from . import views


urlpatterns = [

    #path('', views.home, name="home"),
    path('convenios/list/', ConvenioListView.as_view(), name="convenios_list"), 
    path('convenios/<int:pk>/', ConvenioDetailView.as_view(), name="convenios_detail"), 
    path('convenios/new/', ConvenioCreateView.as_view(), name="convenios_insert"),        
    path('convenios/<int:pk>/update/', ConvenioUpdateView.as_view(), name="convenios_update"),
    path('convenios/<int:pk>/delete/', ConvenioDeleteView.as_view(), name="convenios_delete"),
    path('convenios/export_csv/', views.export_csv, name="export_csv"),

]



 #   path('convenios_delete/<int:id>/', views.convenio_delete, name="convenios_delete"),   #get request to retrieve and display all records
