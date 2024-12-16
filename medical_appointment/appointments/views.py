from django.shortcuts import render, redirect
from .models import Doctor, Symptom, Appointment, Contact
from django.contrib import messages

def home(request):
    symptoms = Symptom.objects.all()
    return render(request, 'appointments/home.html', {'symptoms': symptoms})

def symptoms(request):
    if request.method == 'POST':
        selected_symptoms = request.POST.getlist('symptoms')
        doctors = Doctor.objects.filter(symptom__in=selected_symptoms).distinct()
        return render(request, 'appointments/doctors.html', {'doctors': doctors})
    symptoms = Symptom.objects.all()
    return render(request, 'appointments/symptoms.html', {'symptoms': symptoms})

def doctor_profile(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'appointments/doctor_profile.html', {'doctor': doctor})

def book_appointment(request, doctor_id):
    if request.method == 'POST':
        appointment = Appointment(
            patient_name=request.POST['name'],
            patient_email=request.POST['email'],
            doctor_id=doctor_id,
            date=request.POST['date'],
            time=request.POST['time']
        )
        appointment.save()
        messages.success(request, 'Appointment booked successfully!')
        return redirect('confirmation')
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'appointments/book_appointment.html', {'doctor': doctor})

def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        contact.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    return render(request, 'appointments/contact.html')

def confirmation(request):
    return render(request, 'appointments/confirmation.html')