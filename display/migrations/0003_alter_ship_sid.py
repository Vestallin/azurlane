# Generated by Django 4.1.4 on 2023-03-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_ship_aa_ship_acc_ship_ammo_ship_armor_ship_asw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='sid',
            field=models.CharField(max_length=10, verbose_name='Ship ID'),
        ),
    ]