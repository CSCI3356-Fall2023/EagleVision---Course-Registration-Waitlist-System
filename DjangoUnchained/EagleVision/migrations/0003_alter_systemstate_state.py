# Generated by Django 4.2.6 on 2023-10-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EagleVision', '0002_alter_student_graduation_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemstate',
            name='state',
            field=models.BooleanField(),
        ),
    ]