from django.http.response import HttpResponse
from django.shortcuts import render
from investment.serializers import InvestmentStateSerializer
from investment.models import Investment,InvestmentState
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from investment.serializers import InvestmentSerializer



def home(request):
    return HttpResponse('home')

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes= (IsAuthenticated,)
    filterset_fields = ['ville','etat_d_avancement']



class InvestmentStateViewSet(viewsets.ModelViewSet):
    queryset = InvestmentState.objects.all()
    serializer_class = InvestmentStateSerializer
    permission_classes= (IsAuthenticated,)


    