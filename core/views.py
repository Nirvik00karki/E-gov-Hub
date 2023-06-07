from django.shortcuts import render
from .models import Category, Service


def homepage(request):
    categories = Category.objects.all()
    services = Service.objects.all()

    return render(request, 'homepage.html', {'categories': categories, 'services': services})

# def service_listing(request):
#     services = Service.objects.all()
#     return render(request, 'core/service_listing.html', {'services': services})

# def video_tutorial(request, service_id):
#     service = get_object_or_404(Service, pk=service_id)
#     tutorials = VideoTutorial.objects.filter(service=service)
#     return render(request, 'core/video_tutorial.html', {'service': service, 'tutorials': tutorials})


