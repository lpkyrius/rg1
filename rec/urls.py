from django.urls import path, include

from django.contrib.auth import views as auth_views # "as auth_views" para serparar das views originais

from . import views


urlpatterns = [

    #path('', views.home, name="home"),
    path('convenios_form/', views.convenio_form, name="convenios_insert"),          #get and post request for insert operation
    path('convenios_list/', views.convenio_list, name="convenios_list"),            #get and post request for update operation
    path('convenios_form/<int:id>/', views.convenio_form, name="convenios_update"),   #get request to retrieve and display all records
    path('convenios_delete/<int:id>/', views.convenio_delete, name="convenios_delete"),   #get request to retrieve and display all records
]

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
