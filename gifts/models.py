from django.db import models
from django.urls import reverse

from adverts.models import Advert, Location
from django.utils.translation import gettext_lazy as _


class GiftsType(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('gifts:detail', args=[self.id])


class Gift(Advert, Location):
    """
    handmade
    free classes
    free ticket
    volantir
    pet
    items
    """
    gifts_type = models.ForeignKey(GiftsType, on_delete=models.CASCADE, verbose_name=_('gifts_type'))




