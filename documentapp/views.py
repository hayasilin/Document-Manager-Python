from django.shortcuts import render, redirect
from documentapp.models import document
from documentapp.models import functionModel
from documentapp.form import PostForm

from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def listone(request): 
	try: 
		unit = document.objects.get(cClassName="TestPlayerManager") #讀取一筆資料
	except:
  		errormessage = " (讀取錯誤!)"
	return render(request, "listone.html", locals())

def detail(request, id=None):
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['cId'] #取得表單輸入的編號
		try:
			documents = document.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
			unit = document.objects.get(id=id)
			functions = functionModel.objects.filter(fdocument__id=id).order_by('id')
		except:
			message = "讀取錯誤!"			
	return render(request, "detail.html", locals())	

def listall(request):  
    documents = document.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())
	
def index(request):
    try:
        unit = document.objects.get(cClassName="TestPlayerManager") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    documents = document.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    functions = functionModel.objects.filter(fdocument__id=1).order_by('id')
    return render(request, "index.html", locals())		

def post(request): #新增資料，資料必須驗證
	if request.method == "POST":
		postform = PostForm(request.POST)  #建立forms物件
		if postform.is_valid():			#通過forms驗證
			cClassName = postform.cleaned_data['cClassName'] #取得表單輸入資料
			cClassDescription = postform.cleaned_data['cClassDescription']
			cClassOverview =  postform.cleaned_data['cClassOverview']
			cAuthor = postform.cleaned_data['cAuthor']
			#新增一筆記錄
			unit = document.objects.create(cClassName=cClassName, cClassDescription=cClassDescription, cClassOverview=cClassOverview, cAuthor=cAuthor) 
			unit.save()  #寫入資料庫
			message = '已儲存...'
			return redirect('/listall/')	
		else:
			message = '驗證碼錯誤！'	
	else:
		message = 'Class和Description必須輸入！'
		postform = PostForm()
	return render(request, "post.html", locals())
		
def delete(request,id=None):  #刪除資料
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['cId'] #取得表單輸入的編號
		try:
			unit = document.objects.get(id=id)  
			unit.delete()
			return redirect('/listall/')
		except:
			message = "讀取錯誤!"			
	return render(request, "delete.html", locals())	

def edit(request, id=None, mode=None):
	if mode == "load":
		unit = document.objects.get(id=id)

		return render(request, "edit.html", locals())
	elif mode == "save":
		unit = document.objects.get(id=id)
		unit.cClassName = request.POST['cClassName']
		unit.cClassDescription = request.POST['cClassDescription']
		unit.cClassOverview = request.POST['cClassOverview']
		unit.save()
		message = '已修改...'
		
		return redirect('/listall/')

def postform(request):
	postform = PostForm()
	return render(request, "postform.html", locals())

#會員系統
def addUser(request, username=None, email=None, password=None, mode=None):

	if mode == "load":
		message = "請填寫資料"
		return render(request, "adduser.html", locals())
	else:
		try:
			user = User.objects.get(username = username)
		except:
			user = None

		if user != None:
			message = user.username + " 帳號已建立！"
			return render(request, "adduser.html", locals())
		else:
			user = User.objects.create_user(username, email, password)
			user.first_name = "wen"
			user.last_name = "lin"
			user.is_staff = True
			user.save()

			return redirect('/admin/')

