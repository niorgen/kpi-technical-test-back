# Generated by Django 3.2.7 on 2022-01-13 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0003_alter_investment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='annee_de_livraison',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='codeuai',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='entreprise',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='latitude',
            field=models.FloatField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='longitude',
            field=models.FloatField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='lycee',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='maitrise_d_oeuvre',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='mandataire',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='mode_de_devolution',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='notification_du_marche',
            field=models.DateField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='ppi',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='ville',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
