from rest_framework import routers

from .views import InvestmentViewSet,InvestmentStateViewSet

router = routers.DefaultRouter()
router.register('investments', InvestmentViewSet)
router.register('investments-state', InvestmentStateViewSet)
