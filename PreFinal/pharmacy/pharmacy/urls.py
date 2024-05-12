"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("branches/", views.branches, name="branches"),
    path("appointments/", views.appointments, name="appointments"),
    path("doctors/", views.doctors, name="doctors"),
    path("medsupp/", views.medsupp, name="medsupp"),
    path("medicalhistory/", views.medicalhistory, name="medicalhistory"),
    path("medicines/", views.medicines, name="medicines"),
    path("orders/", views.orders, name="orders"),
    path("patients/", views.patients, name="patients"),
    path("payment/", views.payment, name="payment"),
    path("pharmacists/", views.pharmacists, name="pharmacists"),
    path("policyprovider/", views.policyprovider, name="policyprovider"),
    path("presmedicine/", views.presmedicine, name="presmedicine"),
    path("prescription/", views.prescription, name="prescription"),
    path("stock/", views.stock, name="stock"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("appointments_vacc/", views.appointments_vacc, name="appointments_vacc"),
    path("doctors_query/", views.doctors_query, name="doctors_query"),
    path("total_amount/", views.total_amount, name="total_amount"),
    path("payment_totals/", views.payment_totals, name="payment_totals"),
    path("avg_age/", views.avg_age, name="avg_age"),
    path("comm_pres_med/", views.comm_pres_med, name="comm_pres_med"),
    path("num_pres/", views.num_pres, name="num_pres")

]
