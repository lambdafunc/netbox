# Generated by Django 5.0.9 on 2024-09-26 19:31

import utilities.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0190_nested_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='poweroutlet',
            name='color',
            field=utilities.fields.ColorField(blank=True, max_length=6),
        ),
    ]
