from django.shortcuts import render
from firstapp.models import FirstModel
# Create your views here.

def insertPerson(request):
    person=FirstModel.objects.all()
    return render(request, "home.html",{'people':person})


