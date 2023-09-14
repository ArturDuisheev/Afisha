from django.db import models
from django.utils.translation import gettext_lazy as _

from reccuring.models import BaseModel


class Director(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Имя директора'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'director'
        verbose_name = _('Директор')
        verbose_name_plural = _('Директоры')


class Movie(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Название фильма'))
    description = models.TextField(verbose_name=_('Описание фильма'))
    duration = models.FloatField(verbose_name=_('Продолжительность фильма'))
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name=_('Директор'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movie'
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')
