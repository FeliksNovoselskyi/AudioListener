from django.shortcuts import render

# Create your views here.
def main_func(request):
    return render(request, 'Main/main.html')