# Generated by Django 2.0.9 on 2019-02-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0083_auto_20190220_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultaattype',
            name='_archiefactietermijn',
            field=models.DurationField(editable=False, help_text='De termijn, na het vervallen van het bedrjfsvoeringsbelang, waarna het zaakdossier (de ZAAK met alle bijbehorende INFORMATIEOBJECTen) van een ZAAK met een resultaat van dit RESULTAATTYPE vernietigd of overgebracht (naar een archiefbewaarplaats) moet worden.', null=True, verbose_name='archiefactietermijn'),
        ),
        migrations.AddField(
            model_name='resultaattype',
            name='_archiefnominatie',
            field=models.CharField(choices=[('blijvend_bewaren', 'Het zaakdossier moet bewaard blijven en op de Archiefactiedatum overgedragen worden naar een archiefbewaarplaats.'), ('vernietigen', 'Het zaakdossier moet op of na de Archiefactiedatum vernietigd worden.')], default='', editable=False, help_text='Aanduiding die aangeeft of ZAAKen met een resultaat van dit RESULTAATTYPE blijvend moeten worden bewaard of (op termijn) moeten worden vernietigd .', max_length=20, verbose_name='archiefnominatie'),
        ),
        migrations.AddField(
            model_name='resultaattype',
            name='brondatum_archiefprocedure_afleidingswijze',
            field=models.CharField(choices=[('afgehandeld', 'De termijn start op de datum waarop de zaak is afgehandeld (ZAAK.Einddatum in het RGBZ).'), ('ander_datumkenmerk', 'De termijn start op de datum die is vastgelegd in een ander datumveld dan de datumvelden waarop de overige waarden (van deze attribuutsoort) betrekking hebben. Objecttype, Registratie en Datumkenmerk zijn niet leeg.'), ('eigenschap', 'De termijn start op de datum die vermeld is in een zaaktype-specifieke eigenschap (zijnde een `datumveld`).`ResultaatType.ZaakType` heeft een `Eigenschap`; `Objecttype`, en `Datumkenmerk` zijn niet leeg.'), ('gerelateerde_zaak', 'De termijn start op de datum waarop de gerelateerde zaak is afgehandeld (ZAAK.Einddatum of ZAAK.Gerelateerde_zaak.Einddatum in het RGBZ). `ResultaatType.ZaakType` heeft gerelateerd `ZaakType`'), ('hoofdzaak', 'De termijn start op de datum waarop de gerelateerde zaak is afgehandeld, waarvan de zaak een deelzaak is (ZAAK.Einddatum van de hoofdzaak in het RGBZ).ResultaatType.ZaakType is deelzaaktype van ZaakType'), ('ingangsdatum_besluit', 'De termijn start op de datum waarop het besluit van kracht wordt (BESLUIT.Ingangsdatum in het RGBZ).\tResultaatType.ZaakType heeft relevant BesluitType'), ('termijn', 'De termijn start een vast aantal jaren na de datum waarop de zaak is afgehandeld (ZAAK.Einddatum in het RGBZ).'), ('vervaldatum_besluit', 'De termijn start op de dag na de datum waarop het besluit vervalt (BESLUIT.Vervaldatum in het RGBZ). ResultaatType.ZaakType heeft relevant BesluitType'), ('zaakobject', 'De termijn start op de einddatum geldigheid van het zaakobject waarop de zaak betrekking heeft (bijvoorbeeld de overlijdendatum van een Persoon). ZaakObjectType is relevant voor ResultaatType.ZaakType; Objecttype is niet leeg en komt overeen met de naam van het ZaakObjectType; Datumkenmerk is niet leeg en komt overeen met een attribuutnaam dat bestaat op ZaakObjectType.')], default='', help_text='Wijze van bepalen van de brondatum.', max_length=20, verbose_name='afleidingswijze brondatum'),
            preserve_default=False,
        ),
    ]
