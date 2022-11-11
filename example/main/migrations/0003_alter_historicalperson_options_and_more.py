# Generated by Django 4.0.6 on 2022-11-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_historicalperson_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalperson',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical person', 'verbose_name_plural': 'historical persons'},
        ),
        migrations.AlterModelOptions(
            name='historicalsalemonth',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical sale month', 'verbose_name_plural': 'historical sale months'},
        ),
        migrations.AlterField(
            model_name='historicalperson',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalsalemonth',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]