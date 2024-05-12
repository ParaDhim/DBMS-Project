from django.shortcuts import render
from .models import *
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count, Max, F, Subquery, OuterRef,Q

# Create your views here.
def index(request):
    return render(request, "index.html")

def branches(request):
    branches = Branches.objects.all()
    context = {
        "branches": branches,
    }
    return render(request, "branches.html" , context)

def appointments(request):
    appointments = Appointment.objects.all()
    context = {
        "appointments": appointments,
    }
    return render(request, "appointments.html" , context)

def doctors(request):
    doctors = Doctors.objects.all()
    context = {
        "doctors": doctors,
    }
    return render(request, "doctors.html" , context)

def medsupp(request):
    medsupp = MedSupp.objects.all()
    context = {
        "medsupp": medsupp,
    }
    return render(request, "medsupp.html" , context)

def medicalhistory(request):
    medicalhistory = Medicalhistory.objects.all()
    context = {
        "medicalhistory": medicalhistory,
    }
    return render(request, "medicalhistory.html" , context)

def medicines(request):
    medicines = Medicines.objects.all()
    context = {
        "medicines": medicines,
    }
    return render(request, "medicines.html" , context)

def orders(request):
    orders = Orders.objects.all()
    context = {
        "orders": orders,
    }
    return render(request, "orders.html" , context)

def patients(request):
    patients = Patients.objects.all()
    context = {
        "patients": patients,
    }
    return render(request, "patients.html" , context)

def payment(request):
    payment = Payment.objects.all()
    context = {
        "payment": payment,
    }
    return render(request, "payment.html" , context)

def pharmacists(request):
    pharmacists = Pharmacists.objects.all()
    context = {
        "pharmacists": pharmacists,
    }
    return render(request, "pharmacists.html" , context)

def policyprovider(request):
    policyprovider = Policyprovider.objects.all()
    context = {
        "policyprovider": policyprovider,
    }
    return render(request, "policyprovider.html" , context)

def presmedicine(request):
    presmedicine = PresMedicine.objects.all()
    context = {
        "presmedicine": presmedicine,
    }
    return render(request, "presmedicine.html" , context)

def prescription(request):
    prescription = Prescription.objects.all()
    context = {
        "prescription": prescription,
    }
    return render(request, "prescription.html" , context)

def stock(request):
    stock = Stock.objects.all()
    context = {
        "stock": stock,
    }
    return render(request, "stock.html" , context)

def suppliers(request):
    suppliers = Suppliers.objects.all()
    context = {
        "suppliers": suppliers,
    }
    return render(request, "suppliers.html" , context)

def appointments_vacc(request):
    appointments_vacc = Appointment.objects.filter(reason='Vaccination')
    context = {
        "appointments_vacc": appointments_vacc,
    }
    return render(request, "appointments_vacc.html" , context)

def doctors_query(request):
    doctors_query = Doctors.objects.values('doctor_name_fname', 'doctor_name_lname')
    context = {
        "doctors_query": doctors_query,
    }
    return render(request, "doctors_query.html" , context)

def total_amount(request):
    total_amount = Payment.objects.aggregate(Sum('amount'))['amount__sum']
    context = {
        "total_amount": total_amount,
    }
    return render(request, "total_amount.html" , context)

def payment_totals(request):
    payment_totals = Payment.objects.values('paymentmethod').annotate(total_amount=Sum('amount'))
    context = {
        "payment_totals": payment_totals,
    }
    return render(request, "payment_totals.html" , context)

def avg_age(request):
    avg_age = Patients.objects.filter(appointment__doctorid=69).aggregate(avg_age=Avg('age'))['avg_age']

    context = {
        "avg_age": avg_age,
    }
    return render(request, "avg_age.html" , context)


from django.db import connections

def comm_pres_med(request):
    with connections['mydb'].cursor() as cursor:
        cursor.execute('SELECT Doctors.DoctorID, Doctors.Doctor_Name_Fname,\
                        Doctors.Doctor_Name_Lname, Medicines.Name, COUNT(*) AS PrescriptionCount\
                        FROM Doctors\
                        JOIN Prescription ON Prescription.DoctorID = Doctors.DoctorID\
                        JOIN Medicines ON Medicines.MedicineID = Prescription.MedicineID\
                        GROUP BY Doctors.DoctorID, Medicines.MedicineID\
                        HAVING COUNT(*) = (\
                        SELECT MAX(Count) FROM (\
                        SELECT DoctorID, MedicineID, COUNT(*) AS Count\
                        FROM Prescription\
                        GROUP BY DoctorID, MedicineID\
                        ) AS T\
                        WHERE T.DoctorID = Doctors.DoctorID\
                        );')
        row = cursor.fetchall()
        average_age = row

    context = {'comm_pres_med': average_age}
    return render(request, 'comm_pres_med.html', context)


def num_pres(request):
    with connections['mydb'].cursor() as cursor:
        cursor.execute('SELECT Doctors.Doctor_Name_Fname, Doctors.Doctor_Name_Mname,\
                        Doctors.Doctor_Name_Lname, COUNT(*) AS NumPrescriptions,\
                        SUM(Prescription.Dosage) AS TotalDosage\
                        FROM Doctors\
                        JOIN Prescription ON Prescription.DoctorID = Doctors.DoctorID\
                        JOIN Medicines ON Medicines.MedicineID = Prescription.MedicineID\
                        WHERE Medicines.Type = "Tablet"\
                        GROUP BY Doctors.Doctor_Name_Fname, Doctors.Doctor_Name_Mname,\
                        Doctors.Doctor_Name_Lname\
                        ORDER BY NumPrescriptions DESC;')
        row = cursor.fetchall()
        average_age = row

    context = {'num_pres': average_age}
    return render(request, 'num_pres.html', context)