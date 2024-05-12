from django.shortcuts import render
from .models import *
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count, Max, F, Subquery, OuterRef,Q
from django.db import connection
from django.http import JsonResponse
from .models import Pharmacists
from .forms import UpdateEmailForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from datetime import date
from django.db import connection
from .forms import UpdateSupplierAddressForm
from .forms import PrescriptionForm
from .models import Prescription, Stock,Medicines
from django.db import transaction
from django.shortcuts import get_object_or_404

def homepage(request):
    return render(request, "homepage.html")

def login_signup(request):
    return render(request, "login_signup.html")


def medicine_catalogue(request):
    return render(request, "medicine_catalogue.html")

def map(request):
    branches = Branches.objects.all()
    context = {
        "branches": branches,
    }
    return render(request, "map.html", context)
  

def support(request):
    return render(request, "support.html")

def search(request):
    query = request.GET.get('q')
    if query:
        medicines = Medicines.objects.filter(name__icontains=query)
    else:
        medicines = Medicines.objects.none()
    context = {
        'medicines': medicines,
        'query': query,
    }
    return render(request, 'homepage.html', context)
def searcha(request,patient_id):
    query = request.GET.get('q')
    if query:
        medicines = Medicines.objects.filter(name__icontains=query)
    else:
        medicines = Medicines.objects.all()

    patient = Patients.objects.get(patientid=patient_id)
    context = {
        'query': query,
        'medicines': medicines,
        'patient': patient,
        # ... Other context variables
    }
    return render(request, 'browse_medicines.html', context)


def get_patient_payments(patient_id):
    # Get the orders made by the patient
    patient_orders = Orders.objects.filter(patientid=patient_id)

    # Get the payments for the patient's orders
    patient_payments = Payment.objects.filter(orderid__in=patient_orders)

    return patient_payments

def patient_view(request,patient_id):
    patient = Patients.objects.get(patientid=patient_id)
    medical_history = Medicalhistory.objects.filter(patientid=patient_id)
    policy_provider = Policyprovider.objects.filter(patientid=patient_id)
    appointments = Appointment.objects.filter(patientid=patient_id)
    prescriptions = Prescription.objects.filter(patientid=patient_id)
    orders = Orders.objects.filter(patientid=patient_id)
    patient_payments = get_patient_payments(patient_id)


    context = {
        'patient': patient,
        'medical_history': medical_history,
        'policy_provider': policy_provider,
        'appointments': appointments,
        'prescriptions': prescriptions,
        'orders': orders,
        'patient_payments': patient_payments
    }
    return render(request, "patient_dashboard.html", context)

def doctor_view(request,doctor_id):
    doctor = Doctors.objects.get(doctorid=doctor_id)
    appointments = Appointment.objects.filter(doctorid=doctor_id)
    prescriptions = Prescription.objects.filter(doctorid=doctor_id)
    #doctor_patients = Patients.objects.filter(pk__in=doctor_appointments.values('PatientID'))

    context = {
        'doctor': doctor,
        'appointments': appointments,
        'prescriptions': prescriptions,
    }
    return render(request, "doctor_dashboard.html", context)

def pharmacist_view(request,pharmacist_id):
    pharmacist = Pharmacists.objects.get(pharmacistid=pharmacist_id)
    orders = Orders.objects.filter(pharmacistid=pharmacist_id)
    #branches = Branches.objects.filter(pharmacistid=pharmacist_id)
    stocks = Stock.objects.filter(pharmacistid=pharmacist_id)
    suppliers = Suppliers.objects.all()
    context = {
        'pharmacist': pharmacist,
        'orders': orders,
        #'branches': branches,
        'stocks': stocks,
        'suppliers': suppliers,
    }
    return render(request, "pharmacist_dashboard.html", context)


def transactions(request):
    return render(request, "transaction.html")


def new_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                prescription_data = form.cleaned_data
                new_prescription = Prescription.objects.create(
                    prescriptionid = prescription_data['prescriptionid'],
                    doctorid=prescription_data['doctorid'],
                    patientid=prescription_data['patientid'],
                    medicineid=prescription_data['medicineid'],
                    dosage=prescription_data['dosage'],
                    duration_days=prescription_data['duration_days'],
                    startdate=prescription_data['startdate'],
                    enddate=prescription_data['enddate'],
                    date=prescription_data['date'],
                    datewritten=prescription_data['datewritten']
                )

                # Update stock quantity
                medicine_id = prescription_data['medicineid']
                stock_entry = Stock.objects.filter(medicineid=medicine_id, branchid=1).first()

                if stock_entry:
                    stock_entry.quantity -= 30
                    stock_entry.save()
                else:
                    # Handle the case when the stock entry is not found
                    pass

            return render(request, 'success.html')  # Redirect to a success URL after executing the transaction
    else:
        form = PrescriptionForm()

    return render(request, 'new_prescription.html', {'form': form})



def update_supplier_address(request):
    if request.method == 'POST':
        form = UpdateSupplierAddressForm(request.POST)
        if form.is_valid():
            supplier_id = form.cleaned_data['supplier_id']
            new_address = form.cleaned_data['new_address']

            # Call the stored procedure
            with connection.cursor() as cursor:
                cursor.callproc('example_transaction3')

            return render(request, 'success.html')
    else:
        form = UpdateSupplierAddressForm()

    return render(request, 'update_supplier_address.html', {'form': form})



from .models import Doctors, Patients


def update_contact_numbers(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        patient_contact_number = request.POST['patient_contact_number']
        doctor_id = request.POST['doctor_id']
        doctor_contact_number = request.POST['doctor_contact_number']

        try:
            patient = Patients.objects.get(patientid=patient_id)
            doctor = Doctors.objects.get(doctorid=doctor_id)
        except Patients.DoesNotExist or Doctors.DoesNotExist:
            return render(request, 'update_contact_numbers.html', {'error': 'Invalid patient or doctor ID'})

        patient.contactnumber_number = patient_contact_number
        patient.save()

        doctor.contactnumber_number = doctor_contact_number
        doctor.save()

        return render(request, 'success.html')

    return render(request, 'update_contact_numbers.html')




def update_email_pharmacist(request):
    if request.method == 'POST':
        form = UpdateEmailForm(request.POST)
        if form.is_valid():
            pharmacist_id = form.cleaned_data['pharmacist_id']
            new_email = form.cleaned_data['new_email']
            
            try:
                pharmacist = Pharmacists.objects.get(pharmacistid=pharmacist_id)
                pharmacist.email_address = new_email
                pharmacist.save()
                return render(request, 'success.html')
            except ObjectDoesNotExist:
                form = UpdateEmailForm(request.POST or None)
                return render(request, 'update_email_pharmacist.html', {'form': form, 'error': 'Pharmacist not found.'})
    else:
        form = UpdateEmailForm()
        return render(request, 'update_email_pharmacist.html', {'form': form})
    
def success(request):
    return render(request, 'success.html')

def browse_medicines(request,patient_id):
    medicines = Medicines.objects.all()
    patient = Patients.objects.get(patientid=patient_id)
    context = {
        'medicines': medicines,
        'patient': patient,
    }
    return render(request, 'browse_medicines.html', context)

from django.urls import reverse

def add_to_cart(request,patient_id):
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        quantity = request.POST.get('quantity')
        medicine = Medicines.objects.get(medicineid=medicine_id)
        patient = Patients.objects.get(patientid=patient_id)

        cart_item = Cart(
            PatientID=patient,
            MedicineID=medicine,
            Quantity=quantity,
            Price=medicine.price,
            DateAdded = datetime.now()
        )
        cart_item.save()

    url = reverse('browse_medicines', kwargs={'patient_id': patient_id})
    return redirect(f"{url}")

def view_cart(request, patient_id):
    patient = Patients.objects.get(patientid=patient_id)
    cart_items = Cart.objects.filter(PatientID=patient)
    total_price = sum([item.Price for item in cart_items])
    context = {
        'patient': patient,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'view_cart.html', context)

def place_order(request, patient_id):
    print(patient_id)
    patient = Patients.objects.get(patientid=patient_id)
    
    cart_items = Cart.objects.filter(PatientID=patient)
    print(cart_items)
    if request.method == 'POST':
        
        pharmacist = Pharmacists.objects.get(pharmacistid=1)
        # Iterate through cart items and create new orders
        for item in cart_items:
            order = Orders(
                patientid=patient,
                medicineid=item.MedicineID,
                quantity=item.Quantity,
                date=datetime.today(),
                # ... other order attributes
                pharmacistid = pharmacist,
                deliverystatus = 'Pending',
            )
            order.save()
        
        # Clear the cart
        cart_items.delete()
        
        url = reverse('patient_view', kwargs={'patient_id': patient_id})
        return redirect(f"{url}")
        
    context = {
        'patient': patient,
        'cart_items': cart_items,
    }
    # If the request method is not POST, render the place_order template
    return render(request, 'place_order.html', context)

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicines, medicineid=medicine_id)
    return render(request, 'medicine_detail.html', {'medicine': medicine})