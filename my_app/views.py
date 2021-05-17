from django.shortcuts import render

communication_packages = [
    {'package_name': 'triple',
     'package_price': '159',
     'package_duration': 'year'},
    {'package_name': 'tv_only',
     'package_price': '79',
     'package_duration': 'year'},
    {'package_name': 'internet_only',
     'package_price': '99',
     'package_duration': 'year'},
]


def home(request):
    context = {
        'packages': communication_packages,
        'title': 'Home page'
    }
    return render(request, 'my_app/index.html', context)


def about(request):
    return render(request, 'my_app/about.html', context={'title': 'About page'})
