import pandas as pd
from tcc.services.dicionario import *

class carrega_dados:
    def __init__(self,diretorio):
        self.dados = pd.read_excel(diretorio)

    def buscar_valor(self, dic):

        query = 'Tipo_Cirurgia_Especifica == {} & Tipo_Cirurgia == {} & Hospital == {} & '
        query = query + 'Primeira_Internacao == {} & '
        query = query + 'Acima_70_Anos == {} & T_Ate_Maior_4 == {} & '
        query = query + 'Duracao_Acima_Duas_Horas == {} & '
        query = query + 'Potencial_Contaminacao == {} & Cirurgia_Limpa == {} & '
        query = query + 'Anestesia_Geral == {} & Emergencia == {} & '
        query = query + 'ASA_Maior_2 == {} & Protese == {} & Cirurgia_Videolaparoscopíca == {} & '
        query = query + 'IRIC == {} & Mais_de_Um_Proc == {} & '
        query = query + 'Acima_4_Profissionais == {}'
        query = query.format(dic['tipo_cuirurgia_especifica'],
                             dic['tipo_cirurgia'], dic['hospital'],
                             dic['primeira_internacao'], dic['acima_70_anos'],
                             dic['t_ate_maior_4'],
                             dic['duracao_acima_duas_horas'], dic['potencial_contaminacao'],
                             dic['cirurgia_limpa'], dic['anestesia_geral'], dic['emergencia'],
                             dic['asa_maior_2'], dic['protese'],
                             dic['cirurgia_videolaparoscopica'], dic['iric'],
                             dic['mais_de_um_proc'],
                             dic['acima_4_profissionais'])
        resp = self.dados.query(query)
        infeccao = resp.loc[0, 'Infeccao_Sitio_Cirurgico']
        return (infeccao)