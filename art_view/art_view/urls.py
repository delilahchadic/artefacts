"""
URL configuration for art_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('credits/', views.credits),
    path('people/',views.PersonList.as_view()),
    path('person/<int:person_id>/',views.get_person),
    path('person/works/<int:person_id>/', views.get_works_by_person),
    path('work/<int:work_id>/IIIF/', views.get_iiif),
    path('works/', views.WorkList.as_view()),
    path('person/<int:person_id>/image', views.get_image),
    path('gallery/<int:gallery_id>/', views.get_gallery),
]
