# Generated by Django 3.2.10 on 2022-03-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
