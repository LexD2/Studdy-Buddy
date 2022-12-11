from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('', views.login_page, name='login_page'),
]

