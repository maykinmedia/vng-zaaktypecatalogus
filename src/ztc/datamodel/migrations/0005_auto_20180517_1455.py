# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-17 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import ztc.utils.fields


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0004_auto_20180226_1153")]

    operations = [
        migrations.AddField(
            model_name="besluittype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="besluittype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="eigenschap",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="eigenschap",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="informatieobjecttype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="informatieobjecttype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="informatieobjecttypeomschrijvinggeneriek",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="informatieobjecttypeomschrijvinggeneriek",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="resultaattype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="resultaattype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="roltype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="roltype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="statustype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="statustype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="zaakobjecttype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="zaakobjecttype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="zaaktype",
            name="datum_begin_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="zaaktype",
            name="datum_einde_geldigheid_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop het is opgeheven.",
                null=True,
                verbose_name="datum einde geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="besluittype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="eigenschap",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="informatieobjecttype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="informatieobjecttypeomschrijvinggeneriek",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="resultaattype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="roltype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="statustype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="zaakobjecttype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AlterField(
            model_name="zaaktype",
            name="datum_begin_geldigheid",
            field=ztc.utils.fields.StUFDateField(
                blank=True,
                help_text="De datum waarop het is ontstaan.",
                max_length=9,
                null=True,
                verbose_name="datum begin geldigheid",
            ),
        ),
        migrations.AddField(
            model_name="zaaktype",
            name="versiedatum_new",
            field=models.DateField(
                blank=True,
                help_text="De datum waarop de (gewijzigde) kenmerken van het ZAAKTYPE geldig zijn geworden",
                null=True,
                verbose_name="versiedatum",
            ),
        ),
        migrations.AlterField(
            model_name="zaaktype",
            name="versiedatum",
            field=ztc.utils.fields.DatumField(
                blank=True,
                help_text="De datum waarop de (gewijzigde) kenmerken van het ZAAKTYPE geldig zijn geworden",
                max_length=8,
                null=True,
                verbose_name="versiedatum",
            ),
        ),
    ]
