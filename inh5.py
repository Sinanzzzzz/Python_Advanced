class Hospital:
    def __init__(self):
        self.hospital_name = input("Enter the name of the hospital:")
        self.location = input("Enter the location of the hospital:")
        self.phone = int(input("Enter the phone number of the hospital:"))
        
    def display_hospital(self):
        print("Hostpital name :",self.hospital_name)
        print("Hospital location :",self.location)
        print("Hospital phone number :",self.phone)
        
class Department:
    def __init__(self):
        self.dept_name = input("Enter the name of the department:")
        self.doctor_name = input("Enter the name of the doctor:")
        
    def display_department(self):
        print("Department name :",self.dept_name)
        print("Doctor name :",self.doctor_name)
        
class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name = input("Enter the name of the Patient:")
        self.age = int(input("Enter the age of the Patient:"))
        self.gender = input("Enter the name of the Gender:")
        self.patient_phone = int(input("Enter the phone number of the Patient:"))
        self.adm_date = input("Enter the admission date")
        self.bed_no = int(input("Enter the bed number of the Patient:"))
        self.discharge_date = input("Enter the discharge date:")
        
    def set_discharge(self):
        self.discharge_date = input("Enter the discharge date:")
        
    def full_summary(self):
        print("Patient Summary")
        Hospital.display_hospital(self)
        Department.display_department(self)
        print("Patient name :",self.patient_name)
        print("Age :",self.age)
        print("Gender :",self.gender)
        print("Patient phone number :",self.patient_phone)
        print("Admission date :",self.adm_date)
        print("Bed number :",self.bed_no)
        if(self.discharge_date==""):
            print("Not yet discharged")
        else:
            print("Discharge date :",self.discharge_date)
        
p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()