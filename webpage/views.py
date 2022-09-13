
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world!!!!!!!!!!!!!!!!!!")

def home(request):
    return render(request, "homepage.html")