# Generated by Django 2.2.4 on 2019-11-12 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0117_auto_20191112_0954"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="zaaktype",
            options={
                "ordering": ("catalogus", "identificatie"),
                "verbose_name": "Zaaktype",
                "verbose_name_plural": "Zaaktypen",
            },
        ),
        migrations.RenameField(
            model_name="zaaktype",
            old_name="zaaktype_identificatie",
            new_name="identificatie",
        ),
    ]
