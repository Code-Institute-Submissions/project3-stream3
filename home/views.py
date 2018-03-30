from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")
    
def about(request):
    return render(request, "home/about.html")
    
def hours(request):
    return render(request, "home/hours.html")
