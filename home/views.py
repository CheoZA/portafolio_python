from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def get_curriculum(request):
    return JsonResponse({'nombre':'Felipe Garza'})