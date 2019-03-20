from django.shortcuts import render,redirect
from itertools import chain
# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render_to_response

import random

from 教学管理.models import classmanage, grademanage, users, studentinformation, userteach


def index(request):
	return render(request,'index.html')


def page1(request):
	return render(request,'page1.html')


def classmanages(request):
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

def classdelete(request):
	id = request.GET.get("id")
	classmanage.objects.filter(classnumber=id).delete()
	return redirect('/page10/')

def grade(request):
	if request.method == 'POST':
		stunumber = int(request.POST['stunumber'])
		stuname = request.POST['stuname']
		classnumber = request.POST['classnumber']
		classname = request.POST['classname']
		normalgrade = int(request.POST['normalgrade'])
		testgrade = request.POST['testgrade']

		stunumber = studentinformation.objects.get(stunumber=stunumber)
		classnumber = classmanage.objects.get(classnumber=classnumber)
		if len(grademanage.objects.filter(stunumber=stunumber,classnumber=classnumber)) == 0:
			if True :
				grade =grademanage.objects.create(
					stunumber=stunumber,
					stuname = stuname,
					classnumber = classnumber,
					classname= classname,
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
					'error': '学生或课程不存在！'
				}
				return render(request, 'grade.html', data)
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

def gradedelete(request):
	id = request.GET.get("id")
	grademanage.objects.filter(id=id).delete()
	return redirect('/grade/')

def studentinformations(request):
	if request.method == 'POST':
		stunumber = int(request.POST['stunumber'])
		stuname = request.POST['stuname']
		stusex = request.POST['stusex']
		stuage = int(request.POST['stuage'])
		stuAcademy = request.POST['stuAcademy']
		stuIDcard = request.POST['stuIDcard']

		try:
			stunumber = studentinformation.objects.get(stunumber=stunumber)
		except studentinformation.DoesNotExist:
			information = studentinformation.objects.create(
				stunumber=stunumber,
				stuname = stuname,
				stusex= stusex,
				stuage = stuage,
				stuAcademy = stuAcademy,
				stuIDcard = stuIDcard
			)

			rows = studentinformation.objects.filter()
			data = {
				'tr':rows
			}
			return render(request,'studentinformation.html',data)
		else:
			rows = studentinformation.objects.filter()
			data = {
				'tr': rows,
				'error': '学生信息已存在！'
			}
			return render(request, 'studentinformation.html', data)
	else:
		rows = studentinformation.objects.filter()
		data = {
			'tr': rows
		}
		return render(request,'studentinformation.html',data)


def studentinformationdelete(request):
	id = request.GET.get("id")
	studentinformation.objects.filter(stunumber=id).delete()
	return redirect('/studentinformation/')


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password2 = request.POST['password2']
		sex = request.POST['sex']
		age = request.POST['age']
		img=request.FILES.get('icon')
		name=request.FILES.get('icon').name

		if password != password2:
			return render(request,'index.html',{'error':'两次输入密码不一致！'})



		user = users.objects.create(
			username = username,
			password = password,
			sex = sex,
			age = age,
			img = img,
			name = name
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
			print(user.img.url)
			return render(request,'page1.html',{'user':user})
		else:
			return render(request,'index.html',{'error':'密码错误！'})
	else:
		return render(request,'index.html')


def selectgrade(request):
	if request.method == 'POST':
		stunumber = request.POST['stunumber']
		classnumber = request.POST['classnumber']
		# classAcademy = request.POST['classAcademy']

		try:
			stu = studentinformation.objects.get(stunumber=stunumber)
			clas = classmanage.objects.get(classnumber=classnumber)
		except studentinformation.DoesNotExist:
			return render(request, 'stuclassquery.html', {'error': '学生不存在！'})
		except classmanage.DoesNotExist:
			return render(request, 'stuclassquery.html', {'error': '课程不存在！'})
		else:

			grade1 = grademanage.objects.filter(stunumber=stunumber,classnumber=classnumber)

			data = {
				'tr' : grade1,
			}
			return render(request, 'stuclassquery.html', data)



	else:
		return render(request, 'stuclassquery.html')

def stuclassquerydelete(request):
	id = request.GET.get("id")
	grademanage.objects.filter(id=id).delete()
	return redirect('/stuclassquery/')

def stuinforselect(request):
	if request.method == 'POST':
		stunumber = request.POST['stunumber']
		stunamme = request.POST['stuname']

		try:
			stu = studentinformation.objects.get(stunumber=stunumber)
		except studentinformation.DoesNotExist:
			return render(request, 'stuclassquery.html', {'error': '学生不存在！'})
		else:

			grade1 = studentinformation.objects.filter(stunumber=stunumber)

			data = {
				'tr' : grade1,
			}
			return render(request, 'stuinforselect.html', data)



	else:
		return render(request, 'stuinforselect.html')

def stuinfordelete(request):
	id = request.GET.get("id")
	studentinformation.objects.filter(stunumber=id).delete()
	return redirect('/stuinforselect/')


def userteach1(request):
	if request.method == 'POST':
		classnumber = request.POST['classnumber']
		classname = request.POST['classname']
		classdata = request.POST['classdata']
		classAcademy = request.POST['classAcademy']

		classnumber = classmanage.objects.get(classnumber=classnumber)

		classinformation = userteach.objects.create(
			classnumber = classnumber,
			classname = classname,
			classdata = classdata,
			classAcademy = classAcademy
		)

		rows = userteach.objects.filter()
		data = {
			'tr':rows
		}
		return render(request,'userteach.html',data)


	else:
		rows = userteach.objects.filter()
		data = {
			'tr': rows
		}
		return render(request,'userteach.html',data)


def userteachdelete(request):
	id = request.GET.get("id")
	userteach.objects.filter(id=id).delete()
	return redirect('/userteach/')

def userinfo(request):
	return render(request,'userinfo.html')

def userlogout(request):
	request.session.flush()
	return redirect('/page1/')