from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly

from . import alluploads_settings as alluploads_settings
from .models import AlluploadsImage, AlluploadsFile
from .serializers import AlluploadsImageSerializer, AlluploadsFileSerializer


class AlluploadsImageViewSet(viewsets.ModelViewSet):
    serializer_class = AlluploadsImageSerializer
    queryset = AlluploadsImage.objects.all()

    def get_permissions(self):
        permission_type = alluploads_settings.ALLUPLOADS_PERMISSIONS
        
        if permission_type == 'staff':
            self.permission_classes = (IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, )
            return super(AlluploadsImageViewSet, self).get_permissions()
        elif permission_type == "user":
            self.permission_classes = (IsAuthenticatedOrReadOnly, )
            return super(AlluploadsImageViewSet, self).get_permissions()
        elif permission_type == "default":
            self.permission_classes = (IsAuthenticated, )
            return super(AlluploadsImageViewSet, self).get_permissions()
        else:
            raise serializers.ValidationError({"error": ["wrong value for ALLUPLOADS_PERMISSIONS."]})
    
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        file_serializer = AlluploadsImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'is_selected' not in request.data:
            file_serializer = AlluploadsImageSerializer(instance=instance, data={ 'is_selected': False }, partial=True)
        else:
            file_serializer = AlluploadsImageSerializer(instance=instance, data={'is_selected': request.data['is_selected']}, partial=True)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlluploadsFileViewSet(viewsets.ModelViewSet):
    serializer_class = AlluploadsFileSerializer
    queryset = AlluploadsFile.objects.all()

    def get_permissions(self):
        permission_type = alluploads_settings.ALLUPLOADS_PERMISSIONS
        
        if permission_type == 'staff':
            self.permission_classes = (IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, )
            return super(AlluploadsFileViewSet, self).get_permissions()
        elif permission_type == "user":
            self.permission_classes = (IsAuthenticatedOrReadOnly, )
            return super(AlluploadsFileViewSet, self).get_permissions()
        elif permission_type == "default":
            self.permission_classes = (IsAuthenticated, )
            return super(AlluploadsFileViewSet, self).get_permissions()
        else:
            raise serializers.ValidationError({"error": ["wrong value for ALLUPLOADS_PERMISSIONS."]})

    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        file_serializer = AlluploadsFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'is_selected' not in request.data:
            file_serializer = AlluploadsFileSerializer(instance=instance, data={ 'is_selected': False }, partial=True)
        else:
            file_serializer = AlluploadsFileSerializer(instance=instance, data={'is_selected': request.data['is_selected']}, partial=True)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)