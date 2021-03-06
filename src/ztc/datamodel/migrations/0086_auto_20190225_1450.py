# Generated by Django 2.0.10 on 2019-02-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0085_auto_20190221_1232")]

    operations = [
        migrations.AlterField(
            model_name="resultaattype",
            name="_archiefnominatie",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "blijvend_bewaren",
                        "Het zaakdossier moet bewaard blijven en op de Archiefactiedatum overgedragen worden naar een archiefbewaarplaats.",
                    ),
                    (
                        "vernietigen",
                        "Het zaakdossier moet op of na de Archiefactiedatum vernietigd worden.",
                    ),
                ],
                default="",
                help_text="Aanduiding die aangeeft of ZAAKen met een resultaat van dit RESULTAATTYPE blijvend moeten worden bewaard of (op termijn) moeten worden vernietigd. Indien niet expliciet opgegeven wordt dit gevuld vanuit de selectielijst.",
                max_length=20,
                verbose_name="archiefnominatie",
            ),
        ),
        migrations.AlterField(
            model_name="resultaattype",
            name="brondatum_archiefprocedure_afleidingswijze",
            field=models.CharField(
                choices=[
                    ("afgehandeld", "Afgehandeld"),
                    ("ander_datumkenmerk", "Ander datumkenmerk"),
                    ("eigenschap", "Eigenschap"),
                    ("gerelateerde_zaak", "Gerelateerde zaak"),
                    ("hoofdzaak", "Hoofzaak"),
                    ("ingangsdatum_besluit", "Ingangsdatum besluit"),
                    ("termijn", "Termijn"),
                    ("vervaldatum_besluit", "Vervaldatum besluit"),
                    ("zaakobject", "Zaakobject"),
                ],
                help_text="Wijze van bepalen van de brondatum.",
                max_length=20,
                verbose_name="afleidingswijze brondatum",
            ),
        ),
    ]
