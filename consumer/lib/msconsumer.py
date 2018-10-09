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

class Vereador(object):
	def __init__(self, ver_id, matricula, ver_sexo, ut_id, ini_nome, ini_ativa, ver_nome_completo,
				 ini_codigo_prefeitura, ver_site, ver_biografia, ver_redes_sociais, ver_fone_principal,
				 ver_fones, ver_legislaturas, ver_localizacao, ver_partido, arq_id, arq_id_biografia):
		self.ver_id = ver_id
		self.matricula = matricula
		self.ver_sexo = ver_sexo
		self.ut_id = ut_id
		self.ini_nome = ini_nome
		self.ini_ativa = ini_ativa
		self.ver_nome_completo = ver_nome_completo
		self.ini_codigo_prefeitura = ini_codigo_prefeitura
		self.ver_site = ver_site
		self.ver_biografia = ver_biografia
		self.ver_redes_sociais = ver_redes_sociais
		self.ver_fone_principal = ver_fone_principal
		self.ver_fones = ver_fones
		self.ver_legislaturas = ver_legislaturas
		self.ver_localizacao = ver_localizacao
		self.ver_partido = ver_partido
		self.arq_id = arq_id
		self.arq_id_biografia = arq_id_biografia

class Vereadores_cargo_mesa(object):
	def __init__(self, matricula, ini_nome, crg_nome, crg_ordem):
		self.matricula = matricula
		self.ini_nome = ini_nome
		self.crg_nome = crg_nome
		self.crg_ordem = crg_ordem

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

	# -----------------------------------------------------------------------------------
	# chamada API reunioes comissao pela range de datas
	# -----------------------------------------------------------------------------------
	def consome_reuniao_comissao_range(self, request, data_inicio, data_fim):
		search_url = '{}/api/spl/reuniao_comissao_range/{}/{}/'.format(self.MSCMC_SERVER, data_inicio, data_fim)

		array_json=[]
		r = requests.get(search_url, verify=False)
		reunioes = r.json()

		return JsonResponse(reunioes, safe=False)				

	# -----------------------------------------------------------------------------------
	# chamada API retorna rec_id através pac_id
	# -----------------------------------------------------------------------------------
	def consome_rec_id(self, request, pac_id):
		search_url = '{}/api/spl/spl_get_rec_id/{}/'.format(self.MSCMC_SERVER, pac_id)

		array_json=[]
		r = requests.get(search_url, verify=False)
		rec_id = r.json()
		try:
			result = rec_id[0]['rec_id']
		except:
			result = None

		return result

	# -----------------------------------------------------------------------------------
	# chamada API retorna reuniao atraves rec_id
	# -----------------------------------------------------------------------------------
	def consome_reuniao(self, request, rec_id):
		search_url = '{}/api/spl/spl_get_reuniao/{}/'.format(self.MSCMC_SERVER, rec_id)

		array_json=[]
		r = requests.get(search_url, verify=False)
		reuniao = r.json()
		try:
			result = reuniao[0]
		except:
			result = None

		return result

	# -----------------------------------------------------------------------------------
	# chamada API retorna comissao atraves con_id
	# -----------------------------------------------------------------------------------
	def consome_comissao(self, request, con_id):
		search_url = '{}/api/spl/spl_get_comissao/{}/'.format(self.MSCMC_SERVER, con_id)

		array_json=[]
		r = requests.get(search_url, verify=False)
		comissao = r.json()
		try:
			result = comissao[0]
		except:
			result = None
		return result

	# ----------------------------------------------------------------------------------------------------------------
	# Consome vereadores
	# ----------------------------------------------------------------------------------------------------------------
	def consome_vereadores(self):
		search_url = '{}/api/spl/vereadores/?format=json'.format(self.MSCMC_SERVER)
		r = requests.get(search_url, verify=False)
		vereadores = r.json()

		return JsonResponse(vereadores, safe=False)

	# ----------------------------------------------------------------------------------------------------------------
	# Consome vereador_matricula
	# ----------------------------------------------------------------------------------------------------------------
	def consome_vereador_matricula(self, matricula):
		search_url = '{}/api/spl/vereador_matricula/{}/?format=json'.format(self.MSCMC_SERVER, matricula)
		r = requests.get(search_url, verify=False)
		vereador = r.json()
		try:
			result = vereador[0]
		except:
			result = None
		return result

	# ----------------------------------------------------------------------------------------------------------------
	# Consome vereador_matricula
	# ----------------------------------------------------------------------------------------------------------------
	def consome_cargos_mesa(self):
		retorno = []
		search_url = '{}/api/spl/cargos_mesa/?format=json'.format(self.MSCMC_SERVER)
		r = requests.get(search_url, verify=False)
		cargos_mesa = r.json()

		return JsonResponse(cargos_mesa, safe=False)
