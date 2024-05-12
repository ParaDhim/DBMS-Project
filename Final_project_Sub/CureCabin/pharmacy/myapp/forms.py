from django import forms
from .models import Prescription, Stock, Doctors, Patients, Medicines

class PrescriptionForm(forms.ModelForm):
    prescriptionid = forms.IntegerField()
    doctorid = forms.ModelChoiceField(queryset=Doctors.objects.all())
    patientid = forms.ModelChoiceField(queryset=Patients.objects.all())
    medicineid = forms.ModelChoiceField(queryset=Medicines.objects.all())
    dosage = forms.IntegerField()
    duration_days = forms.IntegerField()
    startdate = forms.DateField()
    enddate = forms.DateField()
    date = forms.DateField()
    datewritten = forms.DateField()

    class Meta:
        model = Prescription
        fields = ['doctorid', 'patientid', 'medicineid', 'dosage', 'duration_days', 'startdate', 'enddate', 'date', 'datewritten']

class UpdateSupplierAddressForm(forms.Form):
    supplier_id = forms.IntegerField()
    new_address = forms.CharField(max_length=100)

    

class UpdateEmailForm(forms.Form):
    pharmacist_id = forms.IntegerField(label='Pharmacist ID', required=True)
    new_email = forms.EmailField(label='New Email Address', required=True)
