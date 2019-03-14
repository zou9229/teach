from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
	return render(request,'index.html')


def page1(request):
	return render(request,'page1.html')


def page10(request):
	row = [
			['row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
			['row 1, cel 2','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1','row 1, cel 1'],
		  ]
	data = {
		'tr':row
	}
	return render(request,'page10.html',data)

def classmanage(request):
	return render(request,'classmanage,html')