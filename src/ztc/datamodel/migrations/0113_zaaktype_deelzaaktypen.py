# Generated by Django 2.2.4 on 2019-10-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0112_auto_20191022_1333")]

    operations = [
        migrations.AddField(
            model_name="zaaktype",
            name="deelzaaktypen",
            field=models.ManyToManyField(
                blank=True,
                help_text="De ZAAKTYPE(n) waaronder ZAAKen als deelzaak kunnen voorkomen bij ZAAKen van dit ZAAKTYPE.",
                related_name="hoofdzaaktypen",
                to="datamodel.ZaakType",
            ),
        )
    ]
