# Generated by Django 3.2.7 on 2022-01-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0004_auto_20220114_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='maitrise_d_oeuvre',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]