from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("포커게임 애플리케이션 개발 위치입니다.")

# Create your views here.
