from rest_framework import serializers
from .models import *

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'

class PassageiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passageiro
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class MotoristaSerializer(serializers.ModelSerializer):
    carro = CarroSerializer()

    class Meta:
        model = Motorista
        fields = '__all__'

    def create(self, validated_data):
        # Separar os dados do carro dos dados do motorista
        carro_data = validated_data.pop('carro')
        
        # Criar o objeto Carro
        carro = Carro.objects.create(**carro_data)
        
        # Criar o objeto Motorista associado ao carro
        motorista = Motorista.objects.create(carro=carro, **validated_data)
        
        return motorista