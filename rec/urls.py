from django.urls import path, include

from django.contrib.auth import views as auth_views # "as auth_views" para serparar das views originais

from . import views


urlpatterns = [

    #path('', views.home, name="home"),
    path('convenios_form/', views.convenio_form, name="convenios_form"),
    path('convenios_list/', views.convenio_list, name="convenios_list"),

]

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
