from django.shortcuts import render,redirect

from django.http import HttpResponse

# from django.contrib.auth.models import User
from .models import CustomUser,Mechanic,Customer


from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    # print(dir(request.user))
    return render(request, 'account/home.html')

def signupopt(request):
    return render(request, 'account/signupOptionPage.html')

def customerSignUp(request):

    if request.method == "POST":

        # alamat = 

        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        atype = request.POST['type']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        myuser = CustomUser.objects.create_user(email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.account_type = atype
        
        myusercustomer = Customer.objects.create(user_profile=myuser)

        myuser.save()
        myusercustomer.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

    return render(request, 'account/signupCust.html')

def mechanicSignUp(request):
    if request.method == "POST":
        mechanic_name = request.POST['mechanic_name']
        email = request.POST['email']
        atype= request.POST['type']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        myuser = CustomUser.objects.create_user(email, password1)
        myuser.first_name = mechanic_name
        
        myuser.account_type = atype
        
        myusermechanic = Mechanic.objects.create(user_profile=myuser)
        myusermechanic.mechanic_name = mechanic_name
        myuser.save()
        myusermechanic.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')
    return render(request, 'account/signupMec.html')

def signin(request):

    if request.method == 'POST':
        
        email = request.POST['email']
        password1 = request.POST['password']
        
    
        user = authenticate(request, email=email, password=password1)

        if user is not None :
            atype = user.account_type
            if atype == 'customer':
                login(request, user)
                fname = user.first_name
                return redirect("indexcustomer")
            else :
                login(request, user)
                fname = user.first_name
                return redirect("indexmechanic")


        else :
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, 'account/signin.html')

def services(request):
    return render(request, 'account/servicespage.html')
    
def aboutus(request):
    return render(request, 'account/aboutus.html')

def contactus(request):
    return render(request, 'account/contact.html')

def indexcustomer(request):
    first_name=request.user.first_name if request.user.is_authenticated else None
    api_key = settings.GOOGLE_MAPS_API_KEY
    return render(request, 'account/login_customer_2.html', {'first_name' : first_name} )

def indexmechanic(request):
    
    first_name=request.user.first_name if request.user.is_authenticated else None
    user = request.user
    mechanic_instance = get_object_or_404(Mechanic, user_profile=user)
    initial_data = {
            'mechanic_name': mechanic_instance.mechanic_name,
            'email': user.email,
            'phone_number': mechanic_instance.phone_number,
            'owner_nik': mechanic_instance.mechanic_nik
        }

    return render(request, 'account/login_mechanic.html', {
        'first_name' : first_name,
        'initial_data' : initial_data
    } )

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('signin')

def mechanicprofile(request):
    user = request.user
    mechanic_instance = get_object_or_404(Mechanic, user_profile=user)

    if request.method == 'GET':
        initial_data = {
            'mechanic_name': mechanic_instance.mechanic_name,
            'email': user.email,
            'phone_number': mechanic_instance.phone_number,
            'owner_nik': mechanic_instance.mechanic_nik
        }
        # Create a form with initial data and pass it to the template for rendering

    if request.method == 'POST'and request.path == '/mechanicprofile':
        mechanic_name = request.POST.get('mechanic_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        owner_nik = request.POST.get('owner_nik')

        # Update the existing mechanic_instance with the new values
        mechanic_instance.mechanic_name = mechanic_name
        mechanic_instance.phone_number = phone_number
        mechanic_instance.mechanic_nik = owner_nik
        mechanic_instance.save()

        return redirect('indexmechanic')

    return render(request, 'account/mechanicprofiles.html', {'initial_data': initial_data})


