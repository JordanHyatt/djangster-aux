# Generated by Django 4.0.6 on 2022-09-01 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_historicalperson_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalperson',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical person'},
        ),
        migrations.AlterField(
            model_name='historicalperson',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtg', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('category', models.CharField(max_length=200)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
        ),
    ]
