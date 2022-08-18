
from django.db import models

# Create your models here.
'''
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
    def __str__(self):
        return self.nome

class Carro(models.Model):
    marca = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    ano = models.DateField()
    def __str__(self):
        return self.marca

'''
### modelos do cms ###

# Create your models here.
class Edital(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    nome = models.CharField(
        max_length=200
    )
    
    class Meta:
        db_table = 'acesso\".\"edital'
        verbose_name_plural = 'Editais'

    


class AreaConhecimento(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    nome = models.CharField(
        max_length=150
    )
    
    class Meta:
        db_table = 'acesso\".\"area_conhecimento'
        verbose_name_plural = 'Áreas de Conhecimento'


class Funcao(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    nome = models.CharField(
        max_length=200
    )
    
    class Meta:
        db_table = 'acesso\".\"funcao'
        verbose_name_plural = 'Funções'
        

class Perfil(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    nome = models.CharField(
        max_length=100
    )
    
    class Meta:
        db_table = 'acesso\".\"perfil'
        verbose_name_plural = 'Perfis'
        
        
class PerfilFuncao(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_funcao = models.ForeignKey(
        Funcao,
        on_delete=models.CASCADE,
        db_column='id_funcao'
    )
    
    id_perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        db_column='id_perfil'
    )
    
    class Meta:
        db_table = 'acesso\".\"perfil_funcao'
        verbose_name_plural = 'Perfil/Função'
        

class Modulo(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    descricao = models.CharField(
        max_length=10
    )
    
    class Meta:
        db_table = 'acesso\".\"modulo'
        verbose_name_plural = 'Módulos'


class Objeto(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_edital = models.ForeignKey(
        Edital,
        on_delete=models.CASCADE,
        db_column='id_edital'
    )
    
    tipo = models.CharField(
        max_length=60
    )
    
    nome = models.CharField(
        max_length=250
    )
    
    etapa_ensino = models.CharField(
        max_length=100
    )
    
    class Meta:
        db_table = 'acesso\".\"objeto'
        verbose_name_plural = 'Objetos'
        

class Trilha(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_area_conhecimento = models.ForeignKey(
        AreaConhecimento,
        on_delete=models.CASCADE,
        db_column='id_area_conhecimento'
    )
    
    titulo = models.CharField(
        max_length=100
    )
    
    edicao = models.CharField(
        max_length=100
    )
    
    objetivo_da_trilha = models.CharField(
        max_length=150
    )
    
    visao_geral = models.CharField(
        max_length=100
    )
    
    class Meta:
        db_table = 'acesso\".\"trilha'
        verbose_name_plural = 'Trilhas'
        

class Topico(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE,
        db_column='id_modulo'
    )
    
    titulo = models.CharField(
        max_length=150
    )
    
    class Meta:
        db_table = 'acesso\".\"topico'
        verbose_name_plural = 'Tópicos'
        

class ModuloPerfil(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        db_column='id_perfil'
    )
    
    id_modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE,
        db_column='id_modulo'
    )
    
    class Meta:
        db_table = 'acesso\".\"modulo_perfil'
        verbose_name_plural = 'Módulo/Perfil'
        

class Usuario(models.Model):
    cpf = models.CharField(
        max_length=11,
        primary_key=True
    )
    
    id_funcao = models.ForeignKey(
        Funcao,
        on_delete=models.CASCADE,
        db_column='id_funcao'
    )
    
    id_area_conhecimento = models.ForeignKey(
        AreaConhecimento,
        on_delete=models.CASCADE,
        db_column='id_area_conhecimento'
    )
    
    id_objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        db_column='id_objeto'
    )
    
    nome = models.CharField(
        max_length=150
    )
    
    email = models.EmailField()
    
    telefone = models.CharField(
        max_length=15
    )
    
    situacao = models.IntegerField()
    
    detalhes = models.CharField(
        max_length=300
    )
    
    class Meta:
        db_table = 'acesso\".\"usuario'
        verbose_name_plural = 'Usuários'


class Curso(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_trilha = models.ForeignKey(
        Trilha,
        on_delete=models.CASCADE,
        db_column='id_trilha'
    )
    
    id_edital = models.ForeignKey(
        Edital,
        on_delete=models.CASCADE,
        db_column='id_edital'
    )
    
    id_objeto = models.ForeignKey(
        Objeto,
        on_delete=models.CASCADE,
        db_column='id_objeto'
    )
    
    titulo = models.CharField(
        max_length=100
    )
    
    id_topico = models.ForeignKey(
        Topico,
        on_delete=models.CASCADE,
        db_column='id_topico'
    )
    
    carga_horaria = models.PositiveIntegerField()
    
    metodologia = models.CharField(
        max_length=50
    )
    
    status = models.CharField(
        max_length=30
    )
    
    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    
    data_criacao = models.DateField()
    
    pre_requisitos = models.CharField(
        max_length=200
    )

    class Meta:
        db_table = 'acesso\".\"curso'
        verbose_name_plural = 'Cursos'        


class UsuarioArea(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    
    id_area = models.ForeignKey(
        AreaConhecimento,
        on_delete=models.CASCADE,
        db_column='id_area'
    )
    
    class Meta:
        db_table = 'acesso\".\"usuario_area'
        verbose_name_plural = 'Usuário/Área'
        

class CursoTrilha(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        db_column='id_curso'
    )
    
    id_trilha = models.ForeignKey(
        Trilha,
        on_delete=models.CASCADE,
        db_column='id_trilha'
    )
    
    class Meta:
        db_table = 'acesso\".\"curso_trilha'
        verbose_name_plural = 'Curso/Trilha'
        

class ModuloCurso(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        db_column='id_curso'
    )
    
    titulo = models.CharField(
        max_length=100
    )
    
    descricao = models.CharField(
        max_length=200
    )
    
    leitura_complementar = models.CharField(
        max_length=200
    )
    
    avaliacao = models.IntegerField()
    
    recuperacao = models.BooleanField(
        default=False
    )
    
    class Meta:
        db_table = 'acesso\".\"modulo_curso'
        verbose_name_plural = 'Modulo/Curso'
        

class Recurso(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        db_column='id_curso'
    )
    
    id_topico = models.ForeignKey(
        Topico,
        on_delete=models.CASCADE,
        db_column='id_topico'
    )
    
    id_modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE,
        db_column='id_modulo'
    )
    
    class Meta:
        db_table = 'acesso\".\"recurso'
        verbose_name_plural = 'Recursos'
        

class Pergunta(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_topico = models.ForeignKey(
        Topico,
        on_delete=models.CASCADE,
        db_column='id_topico'
    )
    
    descricao_pergunta = models.CharField(
        max_length=200
    )
    
    class Meta:
        db_table = 'acesso\".\"pergunta'
        verbose_name_plural = 'Perguntas'
        

class Resposta(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    
    id_pergunta = models.ForeignKey(
        Pergunta,
        on_delete=models.CASCADE,
        db_column='id_pergunta'
    )
    
    descricao = models.CharField(
        max_length=150
    )
    
    resposta_correta = models.BooleanField()
    
    mensagem_erro = models.CharField(
        max_length=300
    )
    
    mensagem_acerto = models.CharField(
        max_length=300
    )
    
    class Meta:
        db_table = 'acesso\".\"resposta'
        verbose_name_plural = 'Respostas'