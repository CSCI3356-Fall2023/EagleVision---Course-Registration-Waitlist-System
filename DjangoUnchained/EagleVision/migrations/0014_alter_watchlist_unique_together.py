# Generated by Django 4.2.6 on 2023-11-27 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EagleVision', '0013_watchlist'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('user', 'course')},
        ),
    ]
