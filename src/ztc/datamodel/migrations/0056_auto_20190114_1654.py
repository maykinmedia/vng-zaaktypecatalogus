# Generated by Django 2.0.9 on 2019-01-14 15:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0055_auto_20190114_1641")]

    operations = [
        migrations.AlterField(
            model_name="zaaktype",
            name="verantwoordingsrelatie",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    max_length=40, verbose_name="verantwoordingsrelatie"
                ),
                blank=True,
                default=list,
                help_text="De relatie tussen ZAAKen van dit ZAAKTYPE en de beleidsmatige en/of financiële verantwoording.",
                size=None,
            ),
        )
    ]
