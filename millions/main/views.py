from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
        return JsonResponse({'foo':'bar'})

def mypageView(request):
    return render(request, 'mypage.html') 