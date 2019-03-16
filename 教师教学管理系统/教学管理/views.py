from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render_to_response

import random

from 教学管理.models import classmanage,grademanage, users


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

		try:
			classnumber = classmanage.objects.get(classnumber=classnumber)
		except classmanage.DoesNotExist:
			grade = classmanage.objects.create(
				classnumber=classnumber,
				classname = classname,
				classteacher = classteacher,
				classgrade = classgrade,
				classAcademy = classAcademy,
				classintroduce = classintroduce
			)

			rows = classmanage.objects.filter()
			data = {
				'tr':rows
			}
			return render(request,'page10.html',data)
		else:
			rows = classmanage.objects.filter()
			data = {
				'tr': rows,
				'error': '课程已存在！'
			}
			return render(request, 'page10.html', data)
	else:
		rows = classmanage.objects.filter()
		data = {
			'tr': rows
		}
		return render(request,'page10.html',data)

def grade(request):
	if request.method == 'POST':
		stunumber = int(request.POST['stunumber'])
		stuname = request.POST['stuname']
		classnumber = request.POST['classnumber']
		normalgrade = int(request.POST['normalgrade'])
		testgrade = request.POST['testgrade']

		classnumber = classmanage.objects.get(classnumber=classnumber)
		if len(grademanage.objects.filter(stunumber=stunumber,classnumber=classnumber)) == 0:
			grade =grademanage.objects.create(
				stunumber=stunumber,
				stuname = stuname,
				classnumber = classnumber,
				normalgrade = normalgrade,
				testgrade = testgrade
			)

			rows = grademanage.objects.filter()
			data = {
				'tr':rows
			}
			return render(request,'grade.html',data)
		else:
			rows = grademanage.objects.filter()
			data = {
				'tr': rows,
				'error': '此记录已存在！'
			}
			return render(request, 'grade.html', data)
	else:
		rows = grademanage.objects.filter()
		data = {
			'tr': rows
		}
		return render(request,'grade.html',data)

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password2 = request.POST['password2']
		sex = request.POST['sex']
		age = request.POST['age']

		if password != password2:
			return render(request,'index.html',{'error':'两次输入密码不一致！'})

		user = users.objects.create(
			username = username,
			password = password,
			sex = sex,
			age = age
		)
		return redirect("/index/")
	else:
		return render(request,'index.html')
	pass

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		try:
			user = users.objects.get(username=username)
		except users.DoesNotExist:
			return render(request,'index.html',{'error':'用户不存在！'})

		if user.password == password:
			request.session['uid'] = user.id
			request.session['username'] = user.username
			return render(request,'page1.html')
		else:
			return render(request,'index.html',{'error':'密码错误！'})
	else:
		return render(request,'index.html')