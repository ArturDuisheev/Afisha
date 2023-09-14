from django.db.models import TextChoices


class StarsRating(TextChoices):
    ONE = '1', 'One stars'
    TWO = '2', 'Two stars'
    THREE = '3', 'Three stars'
    FOUR = '4', 'Four stars'
    FIVE = '5', 'Five stars'
