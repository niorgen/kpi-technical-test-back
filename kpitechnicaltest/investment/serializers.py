from rest_framework import serializers

from investment.models import Investment,InvestmentState

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investment
        fields = "__all__"





class InvestmentStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvestmentState
        fields = "__all__"

