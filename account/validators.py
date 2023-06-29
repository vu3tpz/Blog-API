from django.core.exceptions import ValidationError

from .models import User


def validate_username(username):
    if User.objects.filter(**{f"{User.USERNAME_FIELD}__iexact": username}).exists():
        raise ValidationError(f"User with this {User.USERNAME_FIELD} already exists")
    return username
