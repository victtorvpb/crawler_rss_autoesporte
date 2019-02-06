import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):

        obj, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@admin.com',
                'is_active': True,
                'is_superuser': True,
                'is_staff': True,
            },
        )

        if created:
            obj.set_password('admin')
            obj.save()
