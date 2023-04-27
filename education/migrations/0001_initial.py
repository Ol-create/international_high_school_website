# Generated by Django 4.2 on 2023-04-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcedemicReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=1)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('graduation_year', models.DateField(auto_now_add=True)),
                ('current_occupation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerBaseTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.TimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsAndEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_day', models.DateField(auto_now_add=True)),
                ('class_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer not to say')], default='Prefer not to say', max_length=1)),
            ],
        ),
    ]
