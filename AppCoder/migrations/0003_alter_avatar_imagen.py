# Generated by Django 4.1.2 on 2022-10-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
