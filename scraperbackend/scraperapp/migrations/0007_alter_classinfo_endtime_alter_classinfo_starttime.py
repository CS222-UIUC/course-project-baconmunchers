# Generated by Django 4.1.7 on 2023-03-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraperapp", "0006_alter_classinfo_crn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classinfo",
            name="EndTime",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="classinfo",
            name="StartTime",
            field=models.CharField(max_length=10),
        ),
    ]
