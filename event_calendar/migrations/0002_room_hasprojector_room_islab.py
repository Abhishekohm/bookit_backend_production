# Generated by Django 4.1.1 on 2023-02-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event_calendar", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="hasProjector",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="isLab",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
