# Generated by Django 5.0.3 on 2024-03-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='ranking/'),
        ),
    ]
