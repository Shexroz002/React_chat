from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def not_found(request):
    return render(request, 'not_found.html')
