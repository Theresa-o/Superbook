# Generated by Django 4.1.3 on 2022-12-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="modified",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="note",
            name="title",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
