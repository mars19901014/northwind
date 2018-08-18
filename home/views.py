from django.shortcuts import render
from .models import Customercustomerdemo
from .models import Categories
# Create your views here.


def home(request):
    data = Categories.objects.all().values() 
    return render(request,'home/home.html',locals())

def create(request):
    if request.method == "POST":
        categoryid = request.POST['categoryid']
        categoryname = request.POST['categoryname']
        description = request.POST['description']
        picture = request.POST['picture']
        comment = Categories()
        usercomment = tuple([categoryid,categoryname,description,picture])
        comment.create(usercomment)    
    return render(request,'home/create.html',locals())
### 依照一種敘述(where)刪除資料
# def delete(request):
#     if request.method == "POST":
#         categoryid = request.POST['categoryid']  
#         comment = Categories()
#         usercomment = tuple([categoryid])
#         comment.delete(usercomment)            
#     return render(request,'home/delete.html',locals())

### 依照多種敘述(where)刪除資料
def delete(request):
    if request.method == "POST":
        categoryid = request.POST['categoryid']
        categoryname = request.POST['categoryname']     
        comment = Categories()
        usercomment = tuple([categoryid,categoryname])
        comment.delete(usercomment)            
    return render(request,'home/delete.html',locals())
    

def update(request):
    if request.method == "POST":
        categoryid = request.POST['categoryid']
        categoryname = request.POST['categoryname']
        description = request.POST['description']
        picture = request.POST['picture']
        comment = Categories()
        usercomment = tuple([categoryname,description,picture,categoryid])
        comment.update(usercomment)   
    return render(request,'home/update.html',locals())

### 依照使用者需求,where去查詢
def read(request):
    aaa = Categories.read1()
    if request.method == "POST":
        categoryname = request.POST['categoryname']
        description = request.POST['description']
        comment = Categories()
        usercomment = tuple([categoryname,description])
        # usercomment = tuple([description])
        rows = comment.read(usercomment) 
    return render(request,'home/read.html',locals())

## 將查詢寫死,不用where查詢
# def read(request):
#     rows = Categories.read()
#     return render(request,'home/read.html',locals())


