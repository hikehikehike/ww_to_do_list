# Generated by Django 4.2 on 2023-04-24 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-datetime"]},
        ),
        migrations.RemoveField(
            model_name="task",
            name="deadline",
        ),
    ]
