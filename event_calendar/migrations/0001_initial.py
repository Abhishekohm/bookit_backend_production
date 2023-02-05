# Generated by Django 4.1.1 on 2023-02-04 14:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("committee", "0001_initial"),
        ("faculty", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Holiday",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("capacity", models.IntegerField()),
                (
                    "dept_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="faculty.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Slot",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=5)),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomCalendar",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_calendar.event",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_calendar.room",
                    ),
                ),
                (
                    "slot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_calendar.slot",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="class_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="event_calendar.room"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="committee_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="committee.committee"
            ),
        ),
    ]