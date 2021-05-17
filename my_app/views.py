from django.shortcuts import render
from .models import Package


def home(request):
    context = {
        # 'packages': communication_packages,
        'packages': Package.objects.all(),
        'title': 'Home page'
    }
    return render(request, 'my_app/index.html', context)


def about(request):
    return render(request, 'my_app/about.html', context={'title': 'About page'})
