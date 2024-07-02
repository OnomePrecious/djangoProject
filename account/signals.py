from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from .models import Account


def create_account(self, instance, sender):
    pass