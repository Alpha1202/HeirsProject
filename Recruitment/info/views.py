from django.shortcuts import render
from .models import Applicants


# Create your views here.

def apply(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        position = request.POST['job_position']

        applicant = Applicants(first_name=first_name, last_name=last_name, age=age, position=position)
        applicant.save()
        return render(request, 'success.html')

    else:
        return render(request, 'apply.html')