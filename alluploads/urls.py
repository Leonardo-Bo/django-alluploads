from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AlluploadsImageViewSet, AlluploadsFileViewSet


router = DefaultRouter()
router.register('alluploads-images', AlluploadsImageViewSet, basename='alluploads_images')
router.register('alluploads-files', AlluploadsFileViewSet, basename='alluploads_files')


urlpatterns = [
    path('', include(router.urls)),
]