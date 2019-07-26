from django.shortcuts import render

# Create your views here.


def indexView(request):
    return render(request, 'index.html')

def timerView(request):
    return render(request, 'timer.html')

def communityView(request):
    return render(request, 'community.html')

def aboutView(request):
    return render(request, 'about.html')