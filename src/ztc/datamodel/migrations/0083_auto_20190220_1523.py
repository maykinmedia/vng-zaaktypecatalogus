# Generated by Django 2.0.9 on 2019-02-20 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0082_auto_20190220_1443")]

    operations = [
        migrations.AlterField(
            model_name="resultaattype",
            name="zaaktype",
            field=models.ForeignKey(
                help_text="Het ZAAKTYPE van ZAAKen waarin resultaten van dit RESULTAATTYPE bereikt kunnen worden.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resultaattypen",
                to="datamodel.ZaakType",
                verbose_name="is relevant voor",
            ),
        )
    ]
