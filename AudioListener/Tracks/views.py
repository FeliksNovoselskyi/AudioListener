from django.shortcuts import render

# Create your views here.
def tracks_func(request):
    return render(request, 'Tracks/tracks.html')