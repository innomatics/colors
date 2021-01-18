# Generated by Django 3.1.5 on 2021-01-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("red", models.PositiveSmallIntegerField()),
                ("green", models.PositiveSmallIntegerField()),
                ("blue", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Swatch",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("colors", models.ManyToManyField(to="swatch.Color")),
            ],
        ),
    ]
