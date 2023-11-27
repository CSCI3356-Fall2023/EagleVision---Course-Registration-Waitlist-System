# Generated by Django 4.2.6 on 2023-11-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EagleVision', '0014_alter_watchlist_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=255)),
                ('currentSeats', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('maxSeats', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
            ],
        ),
    ]
