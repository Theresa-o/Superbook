# Generated by Django 4.1.3 on 2022-12-08 03:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("noteapp", "0004_note_image_alter_note_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]