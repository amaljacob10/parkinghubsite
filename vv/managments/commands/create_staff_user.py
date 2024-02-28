# myapp/management/commands/create_staff_user.py
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a staff user and add them to the Staff group'

    def handle(self, *args, **kwargs):
        staff_group, created = Group.objects.get_or_create(name='Staff')

        user = User.objects.create_user(
            username='staff_user',
            password='password123',
        )

        user.groups.add(staff_group)

        self.stdout.write(self.style.SUCCESS('Staff user created successfully.'))
