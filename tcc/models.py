from django.db import models

# Create your models here.
class colunas(object):
    def __init__(self,tipo_cuirurgia_especifica,tipo_cirurgia,hospital,num_internacao, primeira_internacao ,idade_anos,
                 acima_70_anos, t_ate_cirurgia, t_ate_maior_4, duracao_cirurgia, duracao_acima_duas_horas,
                 potencial_contaminacao, cirurgia_limpa, anestesia_geral, emergencia, gravidade_asa, asa_maior_2,
                 protese, cirurgia_videolaparoscopica, iric, num_procedimentos, mais_de_um_proc, num_profissionais_bloco,
                 acima_4_profissionais):

        self.tipo_cuirurgia_especifica = tipo_cuirurgia_especifica
        self.tipo_cirurgia = tipo_cirurgia
        self.hospital = hospital
        self.num_internacao = num_internacao
        self.primeira_internacao = primeira_internacao
        self.idade_anos = idade_anos
        self.acima_70_anos = acima_70_anos
        self.t_ate_cirurgia = t_ate_cirurgia
        self.t_ate_maior_4 = t_ate_maior_4
        self.duracao_cirurgia = duracao_cirurgia
        self.duracao_acima_duas_horas = duracao_acima_duas_horas
        self.potencial_contaminacao = potencial_contaminacao
        self.cirurgia_limpa = cirurgia_limpa
        self.anestesia_geral  = anestesia_geral
        self.emergencia = emergencia
        self.gravidade_asa = gravidade_asa
        self.asa_maior_2 = asa_maior_2
        self.protese = protese
        self.cirurgia_videolaparoscopica = cirurgia_videolaparoscopica
        self.iric = iric
        self.num_procedimentos = num_procedimentos
        self.mais_de_um_proc = mais_de_um_proc
        self.num_profissionais_bloco = num_profissionais_bloco
        self.acima_4_profissionais = acima_4_profissionais




