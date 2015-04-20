from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse("<html><title>Books</title><h1>I've Read</h1></html>")
