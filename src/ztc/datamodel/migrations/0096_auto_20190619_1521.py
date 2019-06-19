# Generated by Django 2.0.13 on 2019-06-19 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0095_merge_20190327_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eigenschap',
            options={'ordering': ('zaaktype', 'eigenschapnaam'), 'verbose_name': 'Eigenschap', 'verbose_name_plural': 'Eigenschappen'},
        ),
        migrations.RenameField(
            model_name='eigenschap',
            old_name='is_van',
            new_name='zaaktype',
        ),
        migrations.AlterUniqueTogether(
            name='eigenschap',
            unique_together={('zaaktype', 'eigenschapnaam')},
        ),
    ]
