import mysql. connector
db = mysql. connector. connect (
    host="localhost",
    user="root",
    passwd="psswd",
    database="curecabin"
)
# sor = db.cursor()
# sor.execute(str)

while True:
    
    print("Enter 1 to write general query!")
    print("Enter 2 to write embed query1 query!")
    print("Enter 3 to write embed query2 query!")
    print("Else No to take Exit")
    st = input()
    if (st == "1"):
        print("Write down your Query!!")
        sor = db.cursor()
        str = input()
        sor.execute(str)
        for i in sor:
            print(i)
        print("=================================================================================================================================================")
    elif(st == "2"):
        sor = db.cursor()
        str = """SELECT Doctors.DoctorID, Doctors.Doctor_Name_Fname,
Doctors.Doctor_Name_Lname, Medicines.Name, COUNT(*) AS PrescriptionCount
FROM Doctors
JOIN Prescription ON Prescription.DoctorID = Doctors.DoctorID
JOIN Medicines ON Medicines.MedicineID = Prescription.MedicineID
GROUP BY Doctors.DoctorID, Medicines.MedicineID

HAVING COUNT(*) = (
SELECT MAX(Count) FROM (
SELECT DoctorID, MedicineID, COUNT(*) AS Count
FROM Prescription
GROUP BY DoctorID, MedicineID
) AS T
WHERE T.DoctorID = Doctors.DoctorID
);"""
        sor.execute(str)
        for i in sor:
            print(i)
        print("=================================================================================================================================================")
    elif(st == "3"):
        sor = db.cursor()
        str = """SELECT Doctors.Doctor_Name_Fname, Doctors.Doctor_Name_Mname,
Doctors.Doctor_Name_Lname, COUNT(*) AS NumPrescriptions,
SUM(Prescription.Dosage) AS TotalDosage
FROM Doctors
JOIN Prescription ON Prescription.DoctorID = Doctors.DoctorID
JOIN Medicines ON Medicines.MedicineID = Prescription.MedicineID
WHERE Medicines.Type = 'Tablet'
GROUP BY Doctors.Doctor_Name_Fname, Doctors.Doctor_Name_Mname,
Doctors.Doctor_Name_Lname
ORDER BY NumPrescriptions DESC;"""
        sor.execute(str)
        for i in sor:
            print(i)
        print("=================================================================================================================================================")
    else:
        break