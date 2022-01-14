# Generated by Django 3.2.7 on 2022-01-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0006_alter_investment_notification_du_marche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='annee_de_livraison',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='codeuai',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='entreprise',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='mandataire',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='ppi',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='ville',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]