from django.db import models



class Investment(models.Model):
    titreoperation = models.CharField(max_length=255)
    entreprise = models.CharField(max_length=255,null=True,default='')
    annee_de_livraison = models.CharField(max_length=50,null=True,default='')
    ville = models.CharField(max_length=100,null=True,default='')
    mandataire = models.CharField(max_length=255,null=True,default='')
    ppi= models.CharField(max_length=50,null=True,default='')
    lycee=models.CharField(max_length=50,null=True,default='')
    notification_du_marche= models.DateField(null=True)
    codeuai=models.CharField(max_length=50,null=True,default='')
    longitude=models.FloatField(null=True,default='')
    latitude=models.FloatField(null=True,default='')
    etat_d_avancement=models.ForeignKey('InvestmentState',null=True, on_delete=models.DO_NOTHING)
    montant_des_ap_votes_en_meu=models.FloatField(null=True)
    cao_attribution=models.DateField(null=True)
    maitrise_d_oeuvre=models.CharField(max_length=255,null=True,default='')
    mode_de_devolution = models.CharField(max_length=50,null=True,default='')
    annee_d_individualisation=models.DateField(null=True)
    enveloppe_prev_en_meu=models.FloatField(null=True)



    
class InvestmentState(models.Model):
    id= models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=50)


    def __str__(self):
        return '{}'.format(self.name)

