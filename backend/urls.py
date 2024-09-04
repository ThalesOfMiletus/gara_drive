from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'motoristas', MotoristaViewSet)
router.register(r'passageiros', PassageiroViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'carros', CarroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
