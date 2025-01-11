import random
from django.core.management.base import BaseCommand
from Forum import user

class Command(BaseCommand):
    help = "Create 1000 users"

    def handle(self, *args, **kwargs):
        users = []
        for i in range(1, 1001):
            user_unit = user.User(
                user_id=i,
                role_id=random.randint(0, 10),
                nickname=f"User{i}",
                description=f"This is user number {i}",
                avatar=f"https://example.com/avatar/{i}",
                login=f"user{i}",
                password=f"password{i}"
            )
            users.append(user_unit)
        user.User.objects.bulk_create(users)
        self.stdout.write("1000 users created successfully!")