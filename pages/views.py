from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render (request, "index.html")

def class11(request):
    return render (request, "class11.html")
def class12(request):
    return render (request, "class12.html")

def result(request):
    return render (request, "result12.html")
def about(request):
    return render (request, "about.html")

def error_404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)