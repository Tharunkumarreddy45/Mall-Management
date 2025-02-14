"""
URL configuration for mallproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mallapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),

    path('adminsignup/', views.sigup),
    path('adminlogin/', views.login),
    path('adminmanageshop/', views.adminmanageshop),
    path('adminmanageoffers/', views.adminmanageoffers),
    path('adminmanagecategoryfloor/', views.adminmanagecategoryfloor),
    path('admincreateshop/', views.admincreateshop),
    path('admincategorywisedetails/', views.admincategorywisedetails),

    path('user/', views.user),
    path('userviewshop/', views.userviewshop),
    path('usershopwiseoffers/', views.usershopwiseoffers),
    path('userlistofshop/', views.userlistofshop),
    path('userfloorwise/', views.userfloorwise),
    


    path('delete/<int:id>', views.delete_shop),
    path('update/<int:id>', views.update_shop),

    path('deleteoffer/<int:id>', views.delete_offer),
    path('updateoffer/<int:id>', views.update_offer),

    path('deletecf/<int:id>', views.delete_cf),

]
