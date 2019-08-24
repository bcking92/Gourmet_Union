# Generated by Django 2.2.4 on 2019-08-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ratings', models.FloatField()),
                ('address', models.TextField()),
                ('food_type', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('service_time', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('picture', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
    ]