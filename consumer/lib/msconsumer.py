import urllib.request
import environ
import simplejson as json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
import requests

class Setor(object):
	def __init__(self, set_id, set_nome, set_sigla, set_id_superior, set_ativo, set_tipo):	
		self.set_id = set_id
		self.set_nome = set_nome
		self.set_sigla = set_sigla
		self.set_id_superior = set_id_superior
		self.set_ativo = set_ativo
		self.set_tipo = set_tipo

class Funcionario(object):
	def __init__(self, matricula, pessoa, pes_nome, funcao, set_id, ind_estagiario):	
		self.matricula = matricula
		self.pessoa = pessoa
		self.pes_nome = pes_nome
		self.funcao = funcao
		self.set_id = set_id
		self.ind_estagiario = ind_estagiario

# ----------------------------------------------------------------------------------------------------------------
# Classe responsável por consumir as informações JSON 
# ----------------------------------------------------------------------------------------------------------------
class MSCMCConsumer(object):

	def __init__(self):
		self.MSCMC_SERVER = settings.MSCMC_SERVER

	# ----------------------------------------------------------------------------------------------------------------
	# Consome o serviço que retorna dados da pessoa através da matrícula
	# ----------------------------------------------------------------------------------------------------------------
	def consome_setor(self, matricula):
		search_url = '{}/api/setor/{}/?format=json'.format(self.MSCMC_SERVER, matricula)
		raw = urllib.request.urlopen(search_url)
		js = raw.readlines()
		js_object = json.loads(js[0])
		return Setor(js_object['set_id'], js_object['set_nome'], js_object['set_sigla'], js_object['set_id_superior'], js_object['set_ativo'], js_object['set_tipo'])

	# ----------------------------------------------------------------------------------------------------------------
	# Consome o serviço que retorna dados do setor atraves codigo do setor
	# ----------------------------------------------------------------------------------------------------------------
	def consome_setor_setor(self,set_id):
		search_url = '{}/api/setor_setor/{}/?format=json'.format(self.MSCMC_SERVER, set_id)
		raw = urllib.request.urlopen(search_url)
		js = raw.readlines()
		js_object = json.loads(js[0])
		return Setor(js_object['set_id'], js_object['set_nome'], js_object['set_sigla'], js_object['set_id_superior'], js_object['set_ativo'], js_object['set_tipo'])		

	# ----------------------------------------------------------------------------------------------------------------
	# Consome setores
	# ----------------------------------------------------------------------------------------------------------------
	def consome_setores(self):
		retorno = []
		search_url = '{}/api/setores/?format=json'.format(self.MSCMC_SERVER)
		raw = urllib.request.urlopen(search_url)
		data = json.load(raw)
		return data

	# ----------------------------------------------------------------------------------------------------------------
	# Consome setores
	# ----------------------------------------------------------------------------------------------------------------
	def consome_setores_combo(self):
		retorno = []
		search_url = '{}/api/setores/?format=json'.format(self.MSCMC_SERVER)
		raw = urllib.request.urlopen(search_url)
		data = json.load(raw)
		return JsonResponse(data, safe=False)

	# ----------------------------------------------------------------------------------------------------------------
	# Consome funcionarios
	# ----------------------------------------------------------------------------------------------------------------
	def consome_funcionarios(self):
		retorno = []
		search_url = '{}/api/funcionarios/?format=json'.format(self.MSCMC_SERVER)
		raw = urllib.request.urlopen(search_url)
		data = json.load(raw)
		return data

	# ----------------------------------------------------------------------------------------------------------------
	# Consome o serviço que retorna dados do funcionario através da chave
	# ----------------------------------------------------------------------------------------------------------------
	def consome_funcionario(self, chave):
		search_url = '{}/api/funcionario/{}/?format=json'.format(self.MSCMC_SERVER, chave)
		raw = urllib.request.urlopen(search_url)
		js = raw.readlines()
		js_object = json.loads(js[0])
		return data

	# -----------------------------------------------------------------------------------
	# chamada API reunioes comissao
	# -----------------------------------------------------------------------------------
	def consome_reuniao_comissao(self):
		search_url = '{}/api/spl/reuniao_comissao/'.format(self.MSCMC_SERVER)

		array_json=[]
		r = requests.get(search_url, verify=False)
		reunioes = r.json()

		return JsonResponse(reunioes, safe=False)				

	# -----------------------------------------------------------------------------------
	# chamada API retorna projeto a partir da pauta e da reuniao
	# -----------------------------------------------------------------------------------
	def consome_projeto(self, request, pac_id, par_id):
		search_url = '{}/api/spl/projeto_reuniao/{}/{}/'.format(self.MSCMC_SERVER, pac_id, par_id)

		array_json=[]
		r = requests.get(search_url, verify=False)
		projeto = r.json()

		return JsonResponse(projeto, safe=False)						

	# -----------------------------------------------------------------------------------
	# chamada API retorna projeto a partir da pauta e da reuniao
	# -----------------------------------------------------------------------------------
	def consome_projetos(self, request, pac_id):
		search_url = '{}/api/spl/projetos_reuniao/{}/'.format(self.MSCMC_SERVER, pac_id)

		array_json=[]
		r = requests.get(search_url, verify=False)
		projetos = r.json()

		return JsonResponse(projetos, safe=False)								
