# Generated by Django 5.0.4 on 2024-04-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datamanagement", "0002_companydatamodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email_address", models.EmailField(max_length=100)),
            ],
        ),
    ]
