from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Students

# Create your views here.
def Index(request):
    return HttpResponse("Hello Python!!!!")

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
#增加学生属性第一种方法
def addStudents(request):
	grade = Grades.objects.get(id=2)
	creatStu = Students.creatStudent('zhangcs',True,25,'wojiaozhangcs',grade)
	creatStu.save()

	return HttpResponse('dsfsafasf')
#增加学生属性第二种方法
def addStudents1(request):
	grade = Grades.objects.get(id=2)
	creatStu = Students.stuManager.creadStudents('zhangcs',True,25,'wojiaozhangcs',grade)
	creatStu.save()

	return HttpResponse('dsfsafasf')

#查询前N条数据
def students1(request):
	studentsList = Students.objects.all()[0:3]

	return render(request, "myApp/students.html", {"students": studentsList})
#分页显示学生
def stupage(request,page):
	page = int(page)
	studentsList = Students.objects.all()[(page-1)*2:2*page]
	return render(request, "myApp/students.html", {"students": studentsList})