"""colors URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .swatch import views

router = routers.DefaultRouter()
router.register(r"swatches", views.SwatchViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
