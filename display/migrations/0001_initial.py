# Generated by Django 4.1.4 on 2023-03-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_name', models.CharField(max_length=255)),
                ('class_name', models.CharField(max_length=10)),
            ],
        ),
    ]
