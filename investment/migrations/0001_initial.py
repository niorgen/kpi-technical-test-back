# Generated by Django 3.2.7 on 2022-01-11 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreoperation', models.CharField(max_length=255)),
                ('entreprise', models.CharField(max_length=100)),
                ('annee_de_livraison', models.CharField(max_length=15)),
                ('ville', models.CharField(max_length=50)),
                ('mandataire', models.CharField(max_length=50)),
                ('ppi', models.CharField(max_length=15)),
                ('lycee', models.CharField(max_length=50)),
                ('notification_du_marche', models.DateField(null=True)),
                ('codeuai', models.CharField(max_length=15)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('montant_des_ap_votes_en_meu', models.FloatField(null=True)),
                ('cao_attribution', models.DateField(null=True)),
                ('maitrise_d_oeuvre', models.CharField(max_length=50)),
                ('mode_de_devolution', models.CharField(max_length=50)),
                ('annee_d_individualisation', models.DateField(null=True)),
                ('enveloppe_prev_en_meu', models.FloatField(null=True)),
                ('etat_d_avancement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='investment.investmentstate')),
            ],
        ),
    ]
