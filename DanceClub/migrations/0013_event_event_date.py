# Generated by Django 3.0.1 on 2020-02-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DanceClub', '0012_auto_20200211_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
