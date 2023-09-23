"""
URL mappings for the image app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from image import views


router = DefaultRouter()
router.register('images', views.ImageViewSet)

app_name = 'image'

urlpatterns = [
    path('', include(router.urls)),
]
