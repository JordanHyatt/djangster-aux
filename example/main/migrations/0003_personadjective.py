# Generated by Django 4.0.6 on 2022-07-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_person_salary_alter_person_middle_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAdjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, unique=True)),
                ('definition', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]