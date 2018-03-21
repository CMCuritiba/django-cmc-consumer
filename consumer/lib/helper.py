from .msconsumer import MSCMCConsumer, Funcionario, Setor

class ServiceHelper(object):
	cons = MSCMCConsumer()

	# ----------------------------------------------------------------------------------------------------------------
	# Retorna setores consumidos
	# ----------------------------------------------------------------------------------------------------------------
	def get_setores(self):
		setores = self.cons.consome_setores()
		objetos_setores = []
		for line in setores:
			objetos_setores.append(Setor(line['set_id'], line['set_nome'], line['set_sigla'], line['set_id_superior'], line['set_ativo'], line['set_tipo']))
		return objetos_setores

	# ----------------------------------------------------------------------------------------------------------------
	# Retorna setor consumido
	# ----------------------------------------------------------------------------------------------------------------
	def get_setor(self,set_id):
		return self.cons.consome_setor_setor(set_id)

	# ----------------------------------------------------------------------------------------------------------------
	# Retorna funcionarios consumidos
	# ----------------------------------------------------------------------------------------------------------------
	def get_funcionarios(self):
		funcionarios = self.cons.consome_funcionarios()
		objetos_funcionarios = []
		for line in funcionarios:
			objetos_funcionarios.append(Funcionario(line['matricula'], line['pessoa'], line['pes_nome'], line['funcao'], line['set_id'], line['ind_estagiario']))
		return objetos_funcionarios

	# ----------------------------------------------------------------------------------------------------------------
	# Retorna funcionario consumido
	# ----------------------------------------------------------------------------------------------------------------		
	def get_funcionario(self, pessoa):
		return self.cons.consome_funcionario(pessoa)

	