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
from .models import CensusData
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session



def homePage(request):
    census = None
    if request.user.is_authenticated:
        # Fetch all entries for the user
        census_entries = CensusData.objects.filter(user=request.user)

        # Use the latest entry by the primary key (nid_or_birth)
        census = census_entries.order_by('-nid_or_birth').first()
    
    return render(request, 'index.html', {'census': census})



def aboutUs(request):
    return render(request, "about.html")

def censusPage(request):
    if request.method == 'POST':
        form = CensusForm(request.POST)
        
        if form.is_valid():
            # Assign the current user to the form before saving
            form.instance.user = request.user
            
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


'''def logOut(request):

    logout(request)
    return redirect('homePage')  # Redirect to homepage or another page after logout'''


def logOut(request):
    # Log out the user
    logout(request)
    # Delete the session if it exists
    if request.session.session_key:
        Session.objects.filter(session_key=request.session.session_key).delete()
    
    return redirect('homePage')

def fetch_realtime_data(request):
    # 1. Total Submissions
    total_submissions = CensusData.objects.count()
    
    # 2. Regions Covered (Unique Districts)
    regions_covered = CensusData.objects.values('city').distinct().count()
    
    # 3. Percentage Completed
    percentage_completed = (total_submissions / 1800) * 100
    
    # 4. Rural Submissions Percentage
    rural_count = CensusData.objects.filter(living_area__icontains="rural").count()
    rural_percentage = (rural_count / total_submissions) * 100 if total_submissions > 0 else 0

    # 5. Urban Submissions Percentage
    urban_percentage = 100 - rural_percentage  # As urban is complementary to rural

    
    # Prepare data for JSON response
    data = {
        'total_submissions': total_submissions,
        'regions_covered': regions_covered,
        'percentage_completed': round(percentage_completed, 2),
        'rural_submissions': round(rural_percentage, 2),
        'urban_submissions': round(urban_percentage, 2),
    }
    return JsonResponse(data)



def update_form(request, pk):
    census_entry = get_object_or_404(CensusData, nid_or_birth=pk, user=request.user)

    if request.method == 'POST':
        form = CensusForm(request.POST, instance=census_entry)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CensusForm(instance=census_entry)

    return render(request, 'update_form.html', {'form': form})


def dashboard_view(request):
    # Ensure user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    # Fetch census data for the logged-in user
    census_entry = get_object_or_404(CensusData, user=request.user)
    
    # Pass data to the template
    context = {
        'user': request.user,
        'census_entry': census_entry,
    }
    return render(request, 'dashboard.html', context)

