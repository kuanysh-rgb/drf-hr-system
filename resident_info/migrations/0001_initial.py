# Generated by Django 4.2.7 on 2023-11-02 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resCountry', models.CharField(max_length=255)),
                ('resRegion', models.CharField(max_length=255)),
                ('resCity', models.CharField(max_length=255)),
            ],
        ),
    ]
