from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ..models import BesluitType
from .mixins import GeldigheidAdminMixin


@admin.register(BesluitType)
class BesluitTypeAdmin(GeldigheidAdminMixin, admin.ModelAdmin):
    # List
    list_display = ('catalogus', 'omschrijving', 'besluitcategorie', )

    # Details
    fieldsets = (
        (_('Algemeen'), {
            'fields': (
                'omschrijving',
                'omschrijving_generiek',
                'besluitcategorie',
                'reactietermijn',
                'toelichting',
            )
        }),
        (_('Publicatie'), {
            'fields': (
                'publicatie_indicatie',
                'publicatietekst',
                'publicatietermijn',
            )
        }),
        (_('Relaties'), {
            'fields': (
                'catalogus',
                'informatieobjecttypes',
            )
        }),
    )
    filter_horizontal = ('informatieobjecttypes', )
