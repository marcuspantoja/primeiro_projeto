from pyexpat import model
from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE,)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __str__(self):
        return self.choice_text

class DadosPessoais(models.Model):
    nome =  models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()    
    
class Carro(models.Model):
    marca = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    ano = models.DateField()
    

