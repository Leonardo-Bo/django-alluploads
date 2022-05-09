from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from .models import AlluploadsImage, AlluploadsFile


class AlluploadsImageSerializer(serializers.ModelSerializer):

    size = serializers.SerializerMethodField()

    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(),
        slug_field='model',
    )

    class Meta:
        model = AlluploadsImage
        fields = ['id', 'parent_dir', 'sub_dir', 'content_type', 'object_id', 'is_selected', 'image', 'size']

    def get_size(self, obj):
        image_size = ''
        if obj.image and hasattr(obj.image, 'size'):
            image_size = obj.image.size
        return image_size

    def to_representation(self, instance):
        response = super(AlluploadsImageSerializer, self).to_representation(instance)
        if instance.image:
            response['image'] = instance.image.url
        return response


class AlluploadsFileSerializer(serializers.ModelSerializer):

    size = serializers.SerializerMethodField()

    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(),
        slug_field='model',
    )

    class Meta:
        model = AlluploadsFile
        fields = ['id', 'parent_dir', 'sub_dir', 'content_type', 'object_id', 'is_selected', 'file', 'size']

    def get_size(self, obj):
        file_size = ''
        if obj.file and hasattr(obj.file, 'size'):
            file_size = obj.file.size
        return file_size

    def to_representation(self, instance):
        response = super(AlluploadsFileSerializer, self).to_representation(instance)
        if instance.file:
            response['file'] = instance.file.url
        return response