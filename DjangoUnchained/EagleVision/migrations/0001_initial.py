# Generated by Django 4.2.7 on 2023-12-05 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(default=models.EmailField(max_length=254, unique=True), max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('department', models.CharField(blank=True, max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(blank=True, choices=[('student', 'Student'), ('admin', 'Admin')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.CharField(default='01/01/2023', max_length=255)),
                ('schedule', models.CharField(default='none', max_length=255)),
                ('instructor', models.CharField(default='none', max_length=255)),
                ('requisite', models.CharField(default='none', max_length=255)),
                ('department', models.CharField(default='none', max_length=255)),
                ('courseIdentifier', models.CharField(default='none', max_length=255)),
                ('max_students_on_watch', models.IntegerField(default=0)),
                ('min_students_on_watch', models.IntegerField(default=0)),
                ('credits', models.CharField(default='3', max_length=10)),
                ('time_slots', models.CharField(default='', max_length=255)),
                ('days', models.CharField(default='none', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(default='', max_length=255, unique=True)),
                ('instructor', models.CharField(default='', max_length=255)),
                ('title', models.CharField(default='', max_length=255)),
                ('location', models.CharField(default='', max_length=255)),
                ('currentSeats', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('maxSeats', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('courseid', models.CharField(default='', max_length=255)),
                ('time', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SystemSnapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('EagleVision.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('major_1', models.CharField(blank=True, max_length=255, null=True)),
                ('major_2', models.CharField(blank=True, max_length=255, null=True)),
                ('major_3', models.CharField(blank=True, max_length=255, null=True)),
                ('minor_1', models.CharField(blank=True, max_length=255, null=True)),
                ('minor_2', models.CharField(blank=True, max_length=255, null=True)),
                ('eagle_id', models.CharField(max_length=50, unique=True)),
                ('graduation_semester', models.CharField(choices=[('Spring2024', 'Spring 2024'), ('Fall2024', 'Fall 2024'), ('Spring2025', 'Spring 2025'), ('Fall2025', 'Fall 2025'), ('Spring2026', 'Spring 2026'), ('Fall2026', 'Fall 2026'), ('Spring2027', 'Spring 2027'), ('Fall2027', 'Fall 2027')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('EagleVision.person',),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EagleVision.course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EagleVision.section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
