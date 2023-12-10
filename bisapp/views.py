
from django.db import IntegrityError
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import IntegrityError
from  .form import SignUpForm
from .models import CustomUser
from .form import UserProfileForm
from .models import UserProfile
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import DocumentRequestForm
from .models import DocumentRequest
from .models import IncidentReport
from .form import IncidentReportForm
from django.shortcuts import get_object_or_404
from .models import Contact







def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            try:
                user = CustomUser.objects.create_user(
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('profileform') 
            except IntegrityError:
                messages.error(request, 'Email or username already exists. Please choose a different one.')

    else:
        form = SignUpForm()

    return render(request, 'SignUp.html', {'form': form})





def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('adminUI') 
            else:
                return redirect('main')  

        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'SignIn.html')



def home(request):

    return render (request, 'BarangayInformationSystem.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('email')
        message = request.POST.get('Message')

        contact_entry = Contact(name=name, email=email, message=message)
        contact_entry.save()

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home') 

    return render(request, 'Contact.html')  

   

def events(request):

    return render (request,'Events.html')


def about(request):

    return render (request,'About.html')


def main(request):

    return render(request,'UserUI.html')



login_required
def profile_form(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    print(f"user_profile: {user_profile}")  

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('main')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'details.html', {'form': form})



    
def request(request):
    if request.method == 'POST':
        form = DocumentRequestForm(request.POST)
        if form.is_valid():
            document_request = form.save(commit=False)
            document_request.user = request.user
            document_request.save()
            return redirect('main')  
    else:
        form = DocumentRequestForm()

    return render(request, 'request.html', {'form': form})



def report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            incident_report = form.save(commit=False)
            incident_report.user = request.user  
            incident_report.save()
            return redirect('main') 
    else:
        form = IncidentReportForm()

    return render(request, 'report.html', {'form': form})

   





def user_logout(request):
    logout(request)
    return redirect(reverse('signin')) 


def request_history(request):
   
    result = DocumentRequest.objects.filter(user=request.user)

    return render(request, 'request_history.html', {'result': result})




def adminUI(request):


    return render (request,'AdminUI.html')





def dashboard(request):

    return render (request,'dashboard.html')


def admin_users(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'Admin_users.html', {'user_profiles': user_profiles})



def admin_users_request(request):
    documents = DocumentRequest.objects.all()

    if request.method == 'POST':
        document_id = request.POST.get('document_id')  
        new_status = request.POST.get('new_status')

        try:
            document = DocumentRequest.objects.get(pk=document_id)  
            document.status = new_status
            document.save()
        except DocumentRequest.DoesNotExist:
            messages.error(request, 'Document not found.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

        return redirect('adminUI')  

    return render(request, 'Admin_users_request.html', {'documents': documents})




def admin_users_report(request):
    incident_reports = IncidentReport.objects.all()

    if request.method == 'POST':
        reporter_id = request.POST.get('reporter_id')  
        new_status = request.POST.get('new_status')

        try:
            incident_report = get_object_or_404(IncidentReport, reporter_id=reporter_id)
            incident_report.status = new_status
            incident_report.save()
            messages.success(request, 'Status updated successfully.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

        return redirect('adminUI')  

    return render(request, 'Admin_users_report.html', {'result': incident_reports})



def report_history(request):
   
    result = IncidentReport.objects.filter(user=request.user)

    return render(request, 'report_history.html', {'result': result})



def message(request):
   
    result = Contact.objects.all()  

    
    context = {'result': result}
    return render(request, 'admin_message.html', context)


def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = CustomUser.objects.get(email=email, first_name=first_name, last_name=last_name)
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please check your information.')
            return redirect('forget')  

        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()

            messages.success(request, 'Password reset successfully. You can now log in with your new password.')
            return redirect('signin') 
        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'forgetpassword.html')



@login_required
def profile(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})