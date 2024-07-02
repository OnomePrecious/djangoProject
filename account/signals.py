from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from .models import Account


@receiver(signal=post_save)
def create_account(self, created, instance, sender=User):
    if created:
        Account.objects.create(user=instance, account_number=instance.phone[1:])

