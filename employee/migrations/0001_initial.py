# Generated by Django 4.1.7 on 2023-02-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("firstName", models.CharField(max_length=40)),
                ("middleName", models.CharField(max_length=40)),
                ("lasstName", models.CharField(max_length=40)),
                ("gender", models.CharField(max_length=40)),
                ("dateBirth", models.DateField()),
                ("contactNumber", models.IntegerField()),
                ("email", models.EmailField(max_length=200)),
            ],
        ),
    ]
