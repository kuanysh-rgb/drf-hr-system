# Generated by Django 4.2.7 on 2023-11-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('military_rank', '0004_militaryrank_nextpromotiondateindays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militaryrank',
            name='nextPromotionDateInDays',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
