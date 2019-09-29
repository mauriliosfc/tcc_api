from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from tcc.services.carrega_dados import *
import json

class BuscarInformacoesView(View):

    template_name = 'index.html'
    def get(self, request):
        return HttpResponse("teste")
    
    # def post(self, request):
    #     return HttpResponse("teste")
    
    def post(self, request):
        carregar = carrega_dados('./tcc/G1.xlsx')
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # print(body)
        # content = body['content']
        # print(content)
        dic = body
        valor = carregar.buscar_valor(dic)
        return HttpResponse(valor)


# from django.shortcuts import render
# from django.views.generic.base import View
# from django.http import HttpResponse
# from django.http import JsonResponse
# from tcc.services.carrega_dados import *

# def index(request):
#     carregar = carrega_dados('C:/Users/gusta/OneDrive/Área de Trabalho/G1/G1 - Base de dados para simulacao.xlsx')
#     # dic = {
#     #     "acima_4_profissionais": 0,
#     #     "acima_70_anos": 0,
#     #     "anestesia_geral": 1,
#     #     "asa_maior_2": 0,
#     #     "cirurgia_limpa": 0,
#     #     "cirurgia_videolaparoscopica": 1,
#     #     "duracao_acima_duas_horas": 1,
#     #     "duracao_cirurgia": 235,
#     #     "emergencia": 0,
#     #     "gravidade_asa": 2,
#     #     "hospital": 4,
#     #     "idade_anos": 42,
#     #     "iric": 0,
#     #     "mais_de_um_proc": 0,
#     #     "num_internacao": 1,
#     #     "num_procedimentos": 1,
#     #     "num_profissionais_bloco": 2,
#     #     "potencial_contaminacao": 4,
#     #     "primeira_internacao": 1,
#     #     "protese": 1,
#     #     "t_ate_cirurgia": 0,
#     #     "t_ate_maior_4": 0,
#     #     "tipo_cirurgia": 2,
#     #     "tipo_cuirurgia_especifica": 1
#     # }

#     valor = carregar.buscar_valor(dic)
#     return HttpResponse(valor)
#     #return JsonResponse({'resp':valor})
#     #return render(request,'index.html')

# def infeccao(request,teste_id):
#     return JsonResponse({'resp':teste_id})
