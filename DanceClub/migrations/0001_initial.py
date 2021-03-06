# Generated by Django 3.0.1 on 2020-02-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('image', models.ImageField(default='img.jpg', upload_to='')),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('booking_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('class_types', models.CharField(max_length=100)),
                ('class_shift', models.CharField(max_length=100)),
                ('booking_date', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bookclass',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.CharField(max_length=100)),
                ('event_date', models.CharField(default='', max_length=100)),
                ('admin_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('set_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('class_types', models.CharField(max_length=100)),
                ('class_shift', models.CharField(default='', max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sets',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('gaurdian_name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.RunSQL("insert into admin(name,email,password,gender,image) values('admin','admin@gmail.com','admin','Male','logo.jpg')")
        
    ]
