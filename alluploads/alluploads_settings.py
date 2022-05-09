from django.conf import settings


def get(key, default):
    return getattr(settings, key, default)

ALLUPLOADS_TREE_STRUCTURE = get('ALLUPLOADS_TREE_STRUCTURE', 1)
ALLUPLOADS_PERMISSIONS = get('ALLUPLOADS_PERMISSIONS', 'default')

