from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import DATABASE
from django.http import HttpResponse


def products_view(request):
    if request.method == 'GET':
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False, 'indent': 4})

def shop_view(request):
    if request.method == 'GET':
        with open('store/shop.html', encoding='utf-8') as f:
            data = f.read()
        return HttpResponse(data)