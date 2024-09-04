from django.db import models


class Carro(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    cor = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
    

class Motorista(models.Model):
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=20, unique=True)
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE)
    disponibilidade = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Passageiro(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    

class Servico(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
    

class Agendamento(models.Model):
    passageiro = models.ForeignKey(Passageiro, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    confirmado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agendamento de {self.passageiro} para {self.servico} em {self.data_hora}"
    

