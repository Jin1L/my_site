# Generated by Django 4.1.2 on 2023-05-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_rename_image_namge_post_image_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image_name",
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="posts"),
        ),
    ]
