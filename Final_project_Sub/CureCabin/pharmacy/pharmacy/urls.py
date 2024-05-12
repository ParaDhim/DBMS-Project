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
    path("", views.search, name="homepage"),
    path('search/', views.search, name='search'),
    path('searcha/<int:patient_id>/', views.searcha, name='searcha'),

    path('login_signup/', views.login_signup, name='login_signup'),
    path('search/login_signup/', views.login_signup, name='login_signup'),
    
     path('patient/<int:patient_id>/', views.patient_view, name='patient_view'),
    path('doctor/<int:doctor_id>/', views.doctor_view, name='doctor_view'),
    path('pharmacist/<int:pharmacist_id>/', views.pharmacist_view, name='pharmacist_view'),
    path('map/', views.map, name='map'),
    path('support/', views.support, name='support'),
    path('search/map/', views.map, name='map'),
    path('search/support/', views.support, name='support'),
    
    path('transactions/', views.transactions, name='transaction'),
    path('search/transactions/', views.transactions, name='transaction'),

    path('update_contact_numbers/', views.update_contact_numbers, name='update_contact_numbers'),
    path('new_prescription/', views.new_prescription, name='new_prescription'),
    path('update_supplier_address/', views.update_supplier_address, name='update_supplier_address'),
    path('update_email_pharmacist/', views.update_email_pharmacist, name='update_email_pharmacist'),

    # path('update_contact_numbers/transactions/', views.transactions, name='update_contact_numbers'),
    # path('new_prescription/transactions/', views.transactions, name='new_prescription'),
    # path('update_supplier_address/transactions/', views.transactions, name='update_supplier_address'),
    # path('update_email_pharmacist/transactions/', views.transactions, name='update_email_pharmacist'),

    path('success/', views.success, name='success'),

    path('browse_medicines/<int:patient_id>/', views.browse_medicines, name='browse_medicines'),
    path('add_to_cart/<int:patient_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/<int:patient_id>/', views.view_cart, name='view_cart'),
    path('place_order/<int:patient_id>/', views.place_order, name='place_order'),
   path('medicine_detail/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
]
