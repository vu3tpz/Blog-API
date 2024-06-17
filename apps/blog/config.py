from djchoices import ChoiceItem, DjangoChoices


class BlogStatusChoices(DjangoChoices):
    """Holds the blog status."""

    draft = ChoiceItem("draft", "Draft")
    under_review = ChoiceItem("under_review", "Under Review")
    withheld = ChoiceItem("withheld", "Withheld")
    publish = ChoiceItem("publish", "Publish")
    reject = ChoiceItem("reject", "Reject")
    appeal = ChoiceItem("appeal", "Appeal")
