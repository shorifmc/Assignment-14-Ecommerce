# Generated by Django 3.2.18 on 2023-03-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=35)),
                ('batch', models.IntegerField()),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
