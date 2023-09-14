from django.db import models
from django.utils.translation import gettext_lazy as _

from reccuring import models as reccuring_models
from my_app.models import Movie
from user_actions import choices as choice


class Review(reccuring_models.BaseModel):
    text = models.TextField(verbose_name=_('комментарий'))
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name=_('Фильм'),
                              related_name="movie_review")
    stars = models.IntegerField(
                                default=choice.StarsRating.ONE,
                                choices=choice.StarsRating.choices,
                                verbose_name=_('Оценка комментария')
                                )

    class Meta:
        ordering = ['created_at']
        db_table = 'reviews'
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
