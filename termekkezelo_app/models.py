from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Termek(models.Model):
    nev = models.CharField('Név', max_length=100)
    leiras = models.CharField('Leírás', max_length=500, blank=True)
    ar = models.DecimalField(
        'Egységár',
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(1000000)],
    )
    keszlet = models.IntegerField('Készlet', validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['id']
        verbose_name = 'termék'
        verbose_name_plural = 'termékek'

    def __str__(self):
        return self.nev