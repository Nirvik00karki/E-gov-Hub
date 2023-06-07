from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('services/', views.service_listing, name='service_listing'),
    # path('tutorial/<int:service_id>/', views.video_tutorial, name='video_tutorial'),
]