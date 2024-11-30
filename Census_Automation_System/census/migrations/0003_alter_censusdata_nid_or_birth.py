# Generated by Django 5.0.6 on 2024-11-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("census", "0002_remove_censusdata_id_censusdata_nid_or_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="censusdata",
            name="nid_or_birth",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=20,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]