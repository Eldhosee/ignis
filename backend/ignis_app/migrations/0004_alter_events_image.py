# Generated by Django 4.0.6 on 2023-08-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ignis_app', '0003_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.URLField(),
        ),
    ]