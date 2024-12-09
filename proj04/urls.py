"""
URL configuration for proj04 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path("start-job/", views.start_job, name="start_job"),
     path("stop-job/<str:job_id>/", views.stop_job, name="stop_job"),
    path("update-job-status/<str:job_id>/", views.update_job_status, name="update_job_status"),
    path("best-distance/<str:weight_type>/", views.best_distance_by_weight_type, name="best_distance"),
    path("", views.index, name="index"),
]

