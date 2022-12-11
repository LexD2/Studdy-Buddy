from django.shortcuts import render, HttpResponse

# Create your views here.


def login_page(request):
    return render(request, 'login_page.html')


def schedule(request):
    return render(request, 'schedule.html')

