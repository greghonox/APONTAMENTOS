from ast import Break
from bdb import Breakpoint
from os import makedirs
from django.db import models
from django.dispatch import receiver
from os.path import join, exists, dirname
from django.db.models.signals import post_save
from core.split_pdf import transforma_pdf_img_funcionarios
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.conf import settings


def caminho_upload(src, instance):
    def verificar_caminho_cria(caminho):
        caminho_arquivo = dirname(join(settings.MEDIA_ROOT, settings.PDFS))
        if not exists(caminho_arquivo):
            try:
                makedirs(caminho_arquivo)
                return True
            except Exception as e:
                print(f"ERRO ENCONTRADO AO TENTAR CRIAR CAMINHO {caminho} {e}")
                return False

    caminho_arquivo = join(settings.PDFS, instance)
    if not verificar_caminho_cria(caminho_arquivo):
        return caminho_arquivo
    return False

class MixData(models.Model):
    data_insercao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Registro"
    )
    data_modificacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Modificação"
    )

    class Meta:
        abstract = True


class Funcionario(AbstractBaseUser):
    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = 'is_anonymous'
    objects = UserManager()
    nome = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True, verbose_name='estado de ativacao')


    def __str__(self): 
        return f"{self.id} {self.nome} {'ativo' if self.status else 'desativo'}"

    # def _create_user(self, username, password):
    #         user = self.model(username=username, status=True)
    #         user.set_password(password)
    #         user.save(using=self._db)
    #         return user

    # def create_user(self, username, password):
    #     return self._create_user(username, password)
    
    # def create_superuser(self, username, password):
    #     user=self._create_user(username, password)
    #     user.save(using=self._db)
    #     return user
    
class FilePdf(MixData):
    caminho_arquivo = models.FileField(upload_to=caminho_upload)

    def __str__(self):
        return f"{self.caminho_arquivo}"


class Holerite(FilePdf):
    mes_choices = (("Jan", "Janeiro"), ("Fev", "Feveiro"), ("Mar", "Março"),
                   ("Abr", "Abril"), ("Mai", "Maio"), ("Jun", "Junho"), ("Jul", "Julho"),
                   ("Ago", "Agosto"), ("Set", "Setembro"), ("Out", "Outubro"),
                   ("Nov", "Novembro"), ("Dez", "Dezembro"),)
    mes = models.CharField(max_length=4, choices=mes_choices,
                           default=mes_choices[0][0],)
    ano = models.IntegerField()
    id_user = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mes} {self.ano} " + super().__str__()


class Ponto(FilePdf):
    mes_choices = (("Jan", "Janeiro"), ("Fev", "Feveiro"), ("Mar", "Março"),
                   ("Abr", "Abril"), ("Mai", "Maio"), ("Jun", "Junho"), ("Jul", "Julho"),
                   ("Ago", "Agosto"), ("Set", "Setembro"), ("Out", "Outubro"),
                   ("Nov", "Novembro"), ("Dez", "Dezembro"),)
    mes = models.CharField(max_length=4, choices=mes_choices,
                           default=mes_choices[0][0],)
    ano = models.IntegerField()
    id_user = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mes} {self.ano} " + super().__str__()
