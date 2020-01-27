# Generated by Django 3.0.1 on 2020-01-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('gaurdian_name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('classes', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]