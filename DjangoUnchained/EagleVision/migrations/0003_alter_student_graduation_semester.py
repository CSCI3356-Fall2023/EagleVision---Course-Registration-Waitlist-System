# Generated by Django 4.2.7 on 2023-12-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EagleVision', '0002_alter_person_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduation_semester',
            field=models.CharField(choices=[('Spring 2024', 'Spring 2024'), ('Fall 2024', 'Fall 2024'), ('Spring 2025', 'Spring 2025'), ('Fall 2025', 'Fall 2025'), ('Spring 2026', 'Spring 2026'), ('Fall 2026', 'Fall 2026'), ('Spring 2027', 'Spring 2027'), ('Fall 2027', 'Fall 2027')], max_length=11),
        ),
    ]
