# Generated by Django 4.2.1 on 2023-05-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="detail",
            field=models.TextField(blank=True, null=True),
        ),
    ]