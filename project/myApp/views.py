from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Students
import os
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'myApp/index.html')
def detail(request,num):
	return HttpResponse("detail-%s"%num)
	
def grades(request):
	#从模型中获取数据
	gradesList = Grades.objects.all()
	#将数据返回至grades.html
	return render(request,"myApp/grades.html",{"grades":gradesList}) 

def students(request):
	#从模型中获取数据
	studentsList = Students.objects.all()
	#将数据返回至grades.html
	return render(request,"myApp/students.html",{"students":studentsList})

def gradesStudents(request,num):
	grade = Grades.objects.get(id=num)
	studentsList = grade.students_set.all()

	return render(request,'myApp/students.html',{'students':studentsList})
#上传文件
def file(request):
	return render(request,'myApp/upfile.html')
def upfile(request):
	#判断是不是post请求
	if request.method == 'POST':
		#上传的文件默认储存在request.FILES中
		f = request.FILES['file']
		#创建路径队形
		filePath = os.path.join(settings.MDEIA_ROOT,f.name)
		#保存文件
		with open(filePath,'wb') as fp:
			#f.chunks()分段上传
			for into in f.chunks():
				fp.write(into)
		return HttpResponse('上传成功')
	else:
		return HttpResponse('不是post请求')