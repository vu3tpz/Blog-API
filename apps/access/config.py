from djchoices import ChoiceItem, DjangoChoices


class UserTypeChoices(DjangoChoices):
    """Holds the user type choices."""

    user = ChoiceItem("user", "User")
    admin = ChoiceItem("admin", "Admin")
