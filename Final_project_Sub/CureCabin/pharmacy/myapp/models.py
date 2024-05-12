from django.db import models

# Create your models here.
class Appointment(models.Model):
    appointmentid = models.IntegerField(db_column='AppointmentID' , primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey('Doctors', models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appointment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Branches(models.Model):
    branchid = models.IntegerField(db_column='BranchID', primary_key=True)  # Field name made lowercase.
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    apt_number = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(db_column='zipCode', max_length=255)  # Field name made lowercase.
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    contactnumber = models.BigIntegerField(db_column='ContactNumber', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branches'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctors(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    doctor_name_fname = models.CharField(db_column='Doctor_Name_Fname', max_length=50)  # Field name made lowercase.
    doctor_name_mname = models.CharField(db_column='Doctor_Name_Mname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doctor_name_lname = models.CharField(db_column='Doctor_Name_Lname', max_length=50)  # Field name made lowercase.
    specialisation_description = models.CharField(db_column='Specialisation_Description', max_length=100)  # Field name made lowercase.
    contactnumber_type = models.CharField(db_column='ContactNumber_type', max_length=20)  # Field name made lowercase.
    contactnumber_number = models.IntegerField(db_column='ContactNumber_number', unique=True)  # Field name made lowercase.
    email_type = models.CharField(db_column='Email_type', max_length=10)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_address', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctors'


class MedSupp(models.Model):
    msid = models.IntegerField(db_column='MSID', primary_key=True)  # Field name made lowercase.
    medicineid = models.ForeignKey('Medicines', models.DO_NOTHING, db_column='MedicineID')  # Field name made lowercase.
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'med_supp'


class Medicalhistory(models.Model):
    medicalhistid = models.IntegerField(db_column='MedicalHistID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicalhistory'


class Medicines(models.Model):
    medicineid = models.IntegerField(db_column='MedicineID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    composition = models.CharField(db_column='Composition', max_length=50)  # Field name made lowercase.
    ingredient = models.CharField(db_column='Ingredient', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=10, decimal_places=2)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=10)  # Field name made lowercase.
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicines'


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    medicineid = models.ForeignKey(Medicines, models.DO_NOTHING, db_column='MedicineID', blank=True, null=True)  # Field name made lowercase.
    pharmacistid = models.ForeignKey('Pharmacists', models.DO_NOTHING, db_column='PharmacistID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.CharField(db_column='DeliveryStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Patients(models.Model):
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    name_fname = models.CharField(db_column='Name_Fname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name_mname = models.CharField(db_column='Name_Mname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name_lname = models.CharField(db_column='Name_Lname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_street_number = models.CharField(db_column='Address_street_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_street_name = models.CharField(db_column='Address_street_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_apt_number = models.CharField(db_column='Address_apt_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_city = models.CharField(db_column='Address_city', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_zipcode = models.IntegerField(db_column='Address_zipCode', blank=True, null=True)  # Field name made lowercase.
    address_state = models.CharField(db_column='Address_state', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_country = models.CharField(db_column='Address_country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    contactnumber_type = models.CharField(db_column='ContactNumber_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactnumber_number = models.IntegerField(db_column='ContactNumber_number', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    email_type = models.CharField(db_column='Email_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patients'


class Payment(models.Model):
    paymentid = models.IntegerField(db_column='PaymentID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=50)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Pharmacists(models.Model):
    pharmacistid = models.IntegerField(db_column='PharmacistID', primary_key=True)  # Field name made lowercase.
    pharmacists_name_fname = models.CharField(db_column='Pharmacists_Name_Fname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pharmacists_name_mname = models.CharField(db_column='Pharmacists_Name_Mname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pharmacists_name_lname = models.CharField(db_column='Pharmacists_Name_Lname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactnumber_type = models.CharField(db_column='ContactNumber_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactnumber_number = models.BigIntegerField(db_column='ContactNumber_number', unique=True, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_type = models.CharField(db_column='Email_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qualification_yearofgraduation = models.IntegerField(db_column='Qualification_yearOfGraduation', blank=True, null=True)  # Field name made lowercase.
    qualification_fieldofstudy = models.CharField(db_column='Qualification_FieldOfStudy', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pharmacists'


class Policyprovider(models.Model):
    policyproviderid = models.IntegerField(db_column='PolicyProviderID', primary_key=True)  # Field name made lowercase.
    policyprovider_name_fname = models.CharField(db_column='PolicyProvider_Name_Fname', max_length=255)  # Field name made lowercase.
    policyprovider_name_mname = models.CharField(db_column='PolicyProvider_Name_Mname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    policyprovider_name_lname = models.CharField(db_column='PolicyProvider_Name_Lname', max_length=255)  # Field name made lowercase.
    contactnumber = models.BigIntegerField(db_column='ContactNumber')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255)  # Field name made lowercase.
    patientid = models.ForeignKey(Patients, models.DO_NOTHING, db_column='PatientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'policyprovider'


class PresMedicine(models.Model):
    pmid = models.IntegerField(db_column='PMID', primary_key=True)  # Field name made lowercase.
    medicineid = models.ForeignKey(Medicines, models.DO_NOTHING, db_column='MedicineID')  # Field name made lowercase.
    prescriptionid = models.ForeignKey('Prescription', models.DO_NOTHING, db_column='PrescriptionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pres_medicine'


class Prescription(models.Model):
    prescriptionid = models.IntegerField(db_column='PrescriptionID', primary_key=True)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='DoctorID')  # Field name made lowercase.
    patientid = models.ForeignKey(Patients, models.DO_NOTHING, db_column='PatientID')  # Field name made lowercase.
    medicineid = models.ForeignKey(Medicines, models.DO_NOTHING, db_column='MedicineID')  # Field name made lowercase.
    dosage = models.IntegerField(db_column='Dosage')  # Field name made lowercase.
    duration_days = models.IntegerField(db_column='Duration_Days')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    datewritten = models.DateField(db_column='DateWritten')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescription'


class Stock(models.Model):
    stockid = models.IntegerField(db_column='StockID' ,primary_key=True)  # Field name made lowercase.
    medicineid = models.ForeignKey(Medicines, models.DO_NOTHING, db_column='MedicineID', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Branches, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    threshold = models.IntegerField(db_column='Threshold', blank=True, null=True)  # Field name made lowercase.
    pharmacistid = models.ForeignKey(Pharmacists, models.DO_NOTHING, db_column='PharmacistID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock'


class Suppliers(models.Model):
    supplierid = models.IntegerField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    supplier_name_fname = models.CharField(db_column='Supplier_Name_Fname', max_length=50)  # Field name made lowercase.
    supplier_name_mname = models.CharField(db_column='Supplier_Name_Mname', max_length=50)  # Field name made lowercase.
    supplier_name_lname = models.CharField(db_column='Supplier_Name_Lname', max_length=50)  # Field name made lowercase.
    contactnumber_type = models.CharField(db_column='ContactNumber_type', max_length=20)  # Field name made lowercase.
    contactnumber_number = models.BigIntegerField(db_column='ContactNumber_number', unique=True, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', unique=True, max_length=50)  # Field name made lowercase.
    email_type = models.CharField(db_column='Email_Type', max_length=20)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    address_type = models.CharField(db_column='Address_Type', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suppliers'

from datetime import datetime
class Cart(models.Model):
    CartID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientID')
    MedicineID = models.ForeignKey('Medicines', models.DO_NOTHING, db_column='MedicineID')
    Quantity = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    DateAdded = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'cart'