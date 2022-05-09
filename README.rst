=====
Alluploads
=====

Alluploads is a Django app to to make uploading files and images easier.

Alluploads is designed to work with django rest framework.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "alluploads" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'alluploads',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('alluploads/', include('alluploads.urls')),

3. Run ``python manage.py migrate`` to create the AlluploadsFile and AlluploadsImage models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to update files and images from admin panel (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/alluploads-images/ to update images or 
   http://127.0.0.1:8000/alluploads-files/ to update files.
