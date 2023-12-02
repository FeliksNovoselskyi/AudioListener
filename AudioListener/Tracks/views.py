from django.shortcuts import render

# Create your views here.
def tracks_func(request):
    return render(request, 'Tracks/tracks.html')


def phonk_func(request):
    return render(request, 'Tracks/phonk.html')

def rock_func(request):
    return render(request, 'Tracks/rock.html')

def jazz_func(request):
    return render(request, 'Tracks/jazz.html')

def heavy_metal_func(request):
    return render(request, 'Tracks/heavy_metal.html')

def classic_func(request):
    return render(request, 'Tracks/classic.html')