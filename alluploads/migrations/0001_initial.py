# Generated by Django 4.0.4 on 2022-05-09 08:46

import alluploads.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlluploadsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_dir', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z_0-9]+\\.?)*[a-zA-Z_0-9]+$')])),
                ('sub_dir', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z_0-9]+\\.?)*[a-zA-Z_0-9]+$')])),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=alluploads.models.image_upload_to)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='AlluploadsFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_dir', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z_0-9]+\\.?)*[a-zA-Z_0-9]+$')])),
                ('sub_dir', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z_0-9]+\\.?)*[a-zA-Z_0-9]+$')])),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to=alluploads.models.file_upload_to)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
