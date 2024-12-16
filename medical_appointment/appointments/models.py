from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    schedule = models.TextField()
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(Doctor)

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.ManyToManyField(Symptom)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()