# Generated by Django 5.0.6 on 2024-06-14 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timestamp', '0002_remove_work_day_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_day',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 14, 12, 11, 55, 519395)),
        ),
    ]