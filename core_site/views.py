from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'core_site/home.html')

def about(request):

    return render(request, 'core_site/about.html')