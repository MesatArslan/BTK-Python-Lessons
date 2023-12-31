# Generated by Django 4.2.7 on 2023-11-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
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
                ("movies_name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.CharField(max_length=100)),
                ("homepage", models.BooleanField(default=False)),
            ],
        ),
    ]

# username:admin
# email adress: info@mesat.com
# password:admin_1234
