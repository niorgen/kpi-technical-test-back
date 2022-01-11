import logging as Log
from datetime import datetime
from django.test import TestCase
from investment.models import Investment


#TODO : Faire les tests
# Create your tests here.
class InvestmentTestCase(TestCase):
    
    def test_add_investment(self):
        nbBeforeAdd = Investment.objects.count()

        new_investment = Investment()
        new_investment.titreoperation = "Investment de test"
        new_investment.entreprise = "Entreprise Name"
        new_investment.annee_de_livraison = datetime.now()
        new_investment.ville = "Ville Name"
        new_investment.mandataire = "Mandataire Name"
        
        new_investment.save()

        nbAfterAdd = Investment.objects.count()
        self.assertTrue(nbAfterAdd == nbBeforeAdd +1)

