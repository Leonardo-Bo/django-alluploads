from django.db import models

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator

from . import alluploads_settings as alluploads_settings


def image_upload_to(instance, filename):

    tree_type = alluploads_settings.ALLUPLOADS_TREE_STRUCTURE

    c1 = instance.parent_dir != None and instance.parent_dir != ''
    c2 = instance.sub_dir != None and instance.sub_dir != ''
    
    if tree_type == 1: 
        if c1:
            if c2:
                return "{}/{}/{}/images/{}/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "{}/{}/{}/images/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )
        else:
            if c2:
                return "{}/{}/images/{}/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "{}/{}/images/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )       
    else:
        if c1:
            if c2:
                return "{}/images/{}/{}/{}/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "{}/images/{}/{}/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )
        else:
            if c2:
                return "images/{}/{}/{}/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "images/{}/{}/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )


def file_upload_to(instance, filename):

    tree_type = alluploads_settings.ALLUPLOADS_TREE_STRUCTURE

    c1 = instance.parent_dir != None and instance.parent_dir != ''
    c2 = instance.sub_dir != None and instance.sub_dir != ''

    if tree_type == 1: 
        if c1:
            if c2:
                return "{}/{}/{}/files/{}/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "{}/{}/{}/files/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )
        else:
            if c2:
                return "{}/{}/files/{}/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "{}/{}/files/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )       
    else:
        if c1: 
            if c2:
                return "{}/files/{}/{}/{}/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "{}/files/{}/{}/{}".format(
                    instance.parent_dir, 
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )
        else:
            if c2: 
                return "files/{}/{}/{}/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    instance.sub_dir,
                    filename
                )
            else: 
                return "files/{}/{}/{}".format(
                    instance.content_type.model,
                    instance.object_id,
                    filename
                )


class AlluploadsImage(models.Model):
    parent_dir = models.CharField(
        max_length=100, 
        validators=[RegexValidator('^([a-zA-Z_0-9]+\.?)*[a-zA-Z_0-9]+$')],
        blank=True,
        null=True
    )
    sub_dir = models.CharField(
        max_length=100, 
        validators=[RegexValidator('^([a-zA-Z_0-9]+\.?)*[a-zA-Z_0-9]+$')],
        blank=True,
        null=True
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    is_selected = models.BooleanField(default=False)

    image = models.ImageField(upload_to=image_upload_to)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class AlluploadsFile(models.Model):
    parent_dir = models.CharField(
        max_length=100, 
        validators=[RegexValidator('^([a-zA-Z_0-9]+\.?)*[a-zA-Z_0-9]+$')],
        blank=True,
        null=True
    )
    sub_dir = models.CharField(
        max_length=100, 
        validators=[RegexValidator('^([a-zA-Z_0-9]+\.?)*[a-zA-Z_0-9]+$')],
        blank=True,
        null=True
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    is_selected = models.BooleanField(default=False)

    file = models.FileField(upload_to=file_upload_to)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
