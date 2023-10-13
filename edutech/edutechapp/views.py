from django.shortcuts import redirect, render

from .models import registration

# Create your views here.
def adminhome(request):
    return render(request,"admin/adminhome.html")

def indexhome(request):
    return render(request,"index/indexhome.html")


def staffhome(request):
    return render(request,"staff/staffhome.html")

def studenthome(request):
    return render(request,"students/studenthome.html")


def registration_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        role = request.POST.getlist('role')
        last_login = request.POST['last_login']
        status = request.POST['status']
        otp = request.POST['otp']
        
        # Create a new registration object and save it to the database
        registration_obj = registration(
            name=name,
            lastname=lastname,
            gender=gender,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            email=email,
            last_login=last_login,
            status=status,
            otp=otp
        )
        registration_obj.save()

        # Add the roles to the registration object
        for r in role:
            registration_obj.role.add(r)

        # Redirect to a success page or do something else
        return redirect('success_page')  # Replace 'success_page' with your actual success page URL

    return render(request, 'index/register.html')