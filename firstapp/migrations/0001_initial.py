# Generated by Django 3.2.8 on 2021-10-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
