from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render_to_response

import random

from 教学管理.models import grademanage


def index(request):
	return render(request,'index.html')


def page1(request):
	return render(request,'page1.html')


def page10(request):
	if request.method == 'POST':
		classnumber = int(request.POST['classnumber'])
		classname = request.POST['classname']
		classteacher = request.POST['classteacher']
		classgrade = int(request.POST['classgrade'])
		classAcademy = request.POST['classAcademy']
		classintroduce = request.POST['classintroduce']


		grade = grademanage.objects.create(
			classnumber=classnumber,
			classname = classname,
			classteacher = classteacher,
			classgrade = classgrade,
			classAcademy = classAcademy,
			classintroduce = classintroduce
		)

		rows = grademanage.objects.filter()
		data = {
			'tr':rows
		}
		return render(request,'page10.html',data)
	else:
		rows = grademanage.objects.filter()
		data = {
			'tr': rows
		}
		return render(request,'page10.html',data)

def classmanage(request):
	return render(request,'classmanage,html')