from django.shortcuts import render
from django.http import HttpResponse
from . models import  *
from manageBed.forms import PatientForm
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

#def addBed(request):
	#return HttpResponse('ELO')




def addPatient(request):

	return render(request, 'addPatient.html')

def displayDoctors(request):

	##list_doctors = Doctor.objects.values('idDoctor', 'firstName', 'middleName', 'lastName')
	doctors = Doctor.objects.all()

	data = {
		 'list_doctors': data
	}

	return JsonResponse(data)

def save(request): 

	if request.method == "POST":
		firstName = request.POST.get('firstName')
		middleName = request.POST.get('middleName')
		lastName = request.POST.get('lastName')
		birthDate = request.POST.get('birthDate')
		religion = request.POST.get('religion')
		minTemp = request.POST.get('minTemp')
		maxTemp = request.POST.get('maxTemp')
		minHeartRate = request.POST.get('minHeartRate')
		maxHeartRate = request.POST.get('maxHeartRate')
		contactNum = request.POST.get('contactNum')
		bedNumber = request.POST.get('bedNumber')

		doctors = request.POST.get('doctors')
		print(doctors)

		patient_var = Patient(firstName = firstName, middleName = middleName, lastName = lastName, birthDate = birthDate, religion = religion, minTemp = minTemp, maxTemp = maxTemp, minHeartRate = minHeartRate, maxHeartRate = maxHeartRate, contactNum = contactNum, bedNumber = bedNumber, status = 1)
		patient_var.save()
	return render(request, 'home.html')
def addDoctor(request):

	if request.method == "POST":
		print("doctor")
		firstName = request.POST.get('firstName')		
		middleName = request.POST.get('middleName')
		lastName = request.POST.get('lastName')
		contactNum = request.POST.get('contactNum')
		username = request.POST.get('username')
		password = request.POST.get('password')

		doctor_var = Doctor(firstName = firstName, middleName = middleName, lastName = lastName, contactNum = contactNum, username = username, password = password)
		doctor_var.save()

	return render(request, 'addDoctor.html')

def listOfPatients(request):

	list_of_patient = Patient.objects.values('idPatient','firstName','lastName')
	print(list_of_patient)
	context = {'list_of_patient':list_of_patient}

	return render(request,'listOfPatients.html',context)

def viewProfile(request, patient_id):
	print(patient_id)

	patient_profile = Patient.objects.filter(idPatient=patient_id).values('idPatient','firstName','lastName','middleName','birthDate','religion','minTemp','maxTemp','minHeartRate','maxHeartRate','doctor','status')
	context = {'patient_profile':patient_profile}

	if request.method == "POST":
		idStatus = request.POST.get('status')
		print(idStatus)
		patient_profile.update(status=idStatus)
#otherwaytoupdate		Patient.objects.filter(idPatient=patient_id).update(status=idStatus)
	return render(request, 'viewProfile.html',context)


def listOfDoctors(request):

	list_of_doctors = Doctor.objects.values('idDoctor','firstName','lastName')
	print(list_of_doctors)
	context = {'list_of_doctors':list_of_doctors}

	return render(request,'listOfDoctors.html',context)

def viewDrProfile(request, doctor_id):
	print(doctor_id)

	doctor_profile = Doctor.objects.filter(idDoctor=doctor_id).values('idDoctor','firstName','lastName','middleName','contactNum','username','password')
	context = {'doctor_profile':doctor_profile}

	if request.method == "POST":
		idStatus = request.POST.get('status')
		print(idStatus)
		patient_profile.update(status=idStatus)
#otherwaytoupdate		Patient.objects.filter(idPatient=patient_id).update(status=idStatus)
	return render(request, 'viewDrProfile.html',context)

def reportListOfPatients(request):

	list_of_patient = Patient.objects.values('idPatient','firstName','lastName')
	print(list_of_patient)
	context = {'list_of_patient':list_of_patient}

	return render(request,'reportListOfPatients.html',context)

def heartRateReport(request,patient_id):

	
	print(patient_id)
	patient_report = HeartRate.objects.filter(idPatient=patient_id).values('heartRate','time','date')
	print(patient_report)
	context = {'patient_report':patient_report}

	if request.method == "POST":	
		date = request.POST.get('date')
		startTime = request.POST.get('startTime')
		endTime = request.POST.get('endTime')
		print(date,startTime,endTime)

		patientd_report = HeartRate.objects.filter(idPatient=patient_id,date=nDate,startTime=startTime).values('heartRate','time')

		context={'patientd_report':patientd_report}
	return render(request,'heartRateReport.html', context)
