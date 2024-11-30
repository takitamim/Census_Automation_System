"""from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CensusData
from .forms import CensusDataForm

def census_form_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        marital_status = request.POST.get('marital_status')
        # Add all other fields in a similar way

        census_data = CensusData(
            full_name=full_name,
            gender=gender,
            dob=dob,
            marital_status=marital_status,
            # Map all other fields here
        )
        census_data.save()

        return redirect('success')
    return render(request, 'census/census_page.html')


def census_form_view(request):
    if request.method == 'POST':
        # Assuming you have a form to handle the census data
        form = CensusDataForm(request.POST)  # Replace with your actual form name

        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page after saving
        else:
            # Handle form errors if necessary
            return render(request, 'census_page.html', {'form': form})  # Render the form with errors

    else:
        form = CensusDataForm()  # Initialize the form
        return render(request, 'census_page.html', {'form': form})"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import CensusForm  # Import the form
from django.http import JsonResponse


def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def censusPage(request):
    if request.method == 'POST':
        form = CensusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page or URL
        else:
            return JsonResponse({'errors': form.errors}, status=400)  # Return errors as JSON
    else:
        form = CensusForm()
    return render(request, 'census_page.html', {'form': form})

def contactSubmit(request):
    return render(request, "contact_submit.html")

def contact(request):
    return render(request, "contact.html")

def faqs(request):
    return render(request, "faqs.html")

def forgotPassword(request):
    return render(request, "Forgot_Password.html")

def help(request):
    return render(request, "help.html")

def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Get the checkbox value

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # Set session expiry to two weeks
            return redirect('censusPage')
        else:
            return render(request, "login.html", {"error": "Email or Password didn't match!"})

    return render(request, "login.html")



def resetPassword(request):
    return render(request, "reset_password.html")


def signUp(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        nid = request.POST['nid_number']

        # Check if password and confirm password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match. Please try again.")
            return redirect('signUp')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please try a different email.")
            return redirect('signUp')

        # Create the user
        user = User.objects.create_user(
            username=email,  # Using email as the username
            email=email,
            password=password
        )
        user.save()

        # Authenticate and log in the user immediately
        user = authenticate(request, username=email, password=password)  # username should be email
        if user is not None:
            login(request, user)
            return redirect('censusPage')
        else:
            messages.error(request, 'Error in logging in. Please try again.')
            return redirect('signUp')

    else:
        return render(request, 'signup.html')



def success(request):
    return render(request, "success.html")   


def logOut(request):
    logout(request)
    return redirect('homePage')  # Redirect to homepage or another page after logout
