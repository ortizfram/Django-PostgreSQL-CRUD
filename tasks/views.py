from django.shortcuts import render


def list_tasks(request):
    return render(request, "list_tasks.html")


def home(request):
    return render(request, "home.html")
