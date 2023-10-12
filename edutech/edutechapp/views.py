from django.shortcuts import render

# Create your views here.
def adminhome(request):
    return render(request,"admin/adminhome.html")

def indexhome(request):
    return render(request,"index/indexhome.html")


def staffhome(request):
    return render(request,"staff/staffhome.html")

def studenthome(request):
    return render(request,"students/studenthome.html")