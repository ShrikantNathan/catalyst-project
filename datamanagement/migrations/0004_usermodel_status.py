# Generated by Django 5.0.4 on 2024-04-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datamanagement", "0003_usermodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]