from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def addData(request):
    return render(request, "addData.html")

def viewdata(request):
    data = Student.objects.all()
    return render(request, "viewdata.html",{"data":data})

def deletedata(request, data_id):
    del_data = Student.objects.get(id=data_id)
    del_data.delete()
    
    return redirect("/viewdata")

def postmethod(request):
    
    request_info = {
        "method" : request.method,
        "user_agent" : request.headers.get('User-Agent', ''),
        'is_authenticated': request.user.is_authenticated,
        "client_ip": request.META.get('REMOTE_ADDR', 'Unknown')
    }
    return render(request, "postmethod.html", {"request_info": request_info})


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")
        number = request.POST.get("number")
        
        if len(request.FILES) !=0:
            image = request.FILES["image"]
        else:
            image = None
        
        student_data = Student(name=name, course=course,email=email,number=number,image=image)
        student_data.save()
    
    return redirect("/viewdata")