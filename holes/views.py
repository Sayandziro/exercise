from django.shortcuts import render


def hole(request):
    return render(request, "holes/hole.html")

