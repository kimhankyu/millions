#main/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.


def indexView(request):
    return render(request, 'index.html')

def timerView(request):
    return render(request, 'timer.html')

def aboutView(request):
    return render(request, 'about.html')

def dataView(request):
    if request.method == 'POST':
        print(request.body)
        return JsonResponse({'foo': 'bar'})

@login_required
def mypageView(request):
    

    return render(request, 'mypage.html') 