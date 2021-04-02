from django.shortcuts import render
from django.http import HttpResponse
def a(b):
    return HttpResponse('<marquee scrollamount="30"><h1 style="color: red ;">vishwa reddy ngbt bec mech pyspi python fullstack developer</h1></marquee>')
def v(n):
    return render(n,'ht.html')

# Create your views here.
