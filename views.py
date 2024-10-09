from django.shortcuts import render
from .models import MyModel
from .forms import forms
from datetime import date

def example_view(request):
    entries = MyModel.objects.all()
    return render(request, 'index.html', {'entries': entries})


# Create your views here.
def index(request):
    return render(request,'index.html')

# MyApp/views.py
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError

def bad_request(request, exception=None):
    return HttpResponseBadRequest("Custom 400 error message")

def permission_denied(request, exception=None):
    return HttpResponseForbidden("Custom 403 error message")

def page_not_found(request, exception=None):
    return HttpResponseNotFound("Custom 404 error message")

def server_error(request):
    return HttpResponseServerError("Custom 500 error message")


# Form Submission
from django.shortcuts import render
from .forms import MyModelForm

def create_appointment(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.instance.sr_no = MyModel.objects.count() + 1  # Automatically set Sr. No
            form.save()
            # After saving the form, you can either show a success message or just show the form again
            return render(request, 'appointment_form.html', {
                'form': form,
                'message': 'Appointment request submitted successfully!',
            })
    else:
        form = MyModelForm()

    return render(request, 'appointment_form.html', {'form': form})


# views.py
def my_view(request):
    form = froms()

    
    context = {
        'form': form,
        'today': date.today(),  
    }

    return render(request, 'your_template.html', context)
