from django.core.exceptions import ValidationError


def validate_pin(pin):
    if len(pin) < 4:
        raise ValidationError("Pin must be four digits")


def validate_account_number(account_number):
    if len(account_number) > 10:
        raise ValidationError("Account number must be ten digits")
