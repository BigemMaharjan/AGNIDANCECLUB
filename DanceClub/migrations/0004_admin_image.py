# Generated by Django 3.0.1 on 2020-02-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DanceClub', '0003_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='image',
            field=models.ImageField(default='img.jpg', upload_to=''),
        ),
    ]
