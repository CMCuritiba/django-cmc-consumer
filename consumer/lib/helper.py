from .msconsumer import MSCMCConsumer, Funcionario, Setor, Vereador, Vereadores_cargo_mesa

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

    # ----------------------------------------------------------------------------------------------------------------
    # Retorna setores consumidos formatados para combo box
    # ----------------------------------------------------------------------------------------------------------------
    def get_setores_combo(self, inicial):
        setores = self.cons.consome_setores()
        objetos_setores = []
        objetos_setores.append(Setor(None, inicial, inicial, None, None, None))
        for line in setores:
            objetos_setores.append(Setor(line['set_id'], line['set_nome'], line['set_sigla'], line['set_id_superior'], line['set_ativo'], line['set_tipo']))
        return objetos_setores

    # ----------------------------------------------------------------------------------------------------------------
    # Retorna textos de conclusão dos projetos
    # ----------------------------------------------------------------------------------------------------------------      
    def get_textos_conclusao(self, pro_codigo):
        return self.cons.consome_textos_conclusao(pro_codigo)

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

    # ----------------------------------------------------------------------------------------------------------------
    # Retorna setores consumidos formatados para combo box
    # ----------------------------------------------------------------------------------------------------------------
    def get_setores_combo(self, inicial):
        setores = self.cons.consome_setores()
        objetos_setores = []
        objetos_setores.append(Setor(None, inicial, inicial, None, None, None))
        for line in setores:
            objetos_setores.append(Setor(line['set_id'], line['set_nome'], line['set_sigla'], line['set_id_superior'], line['set_ativo'], line['set_tipo']))
        return objetos_setores

    # ----------------------------------------------------------------------------------------------------------------
    # Retorna vereadores ativos no SPL
    # Para completar as informações usadas no RAMAIS -- com nome político e nome completo dos vereadores
    # ----------------------------------------------------------------------------------------------------------------
    def get_spl_vereadores_ativos(self):
        vereadores = self.cons.consome_vereadores()
        objetos_vereadores = []
        for line in vereadores:
            if line['ini_ativa'] == True:
                objetos_vereadores.append(Vereador(line['ver_id'], line['matricula'], line['ini_nome'],
                                                   line['ver_nome_completo']))
        return objetos_vereadores

    # ----------------------------------------------------------------------------------------------------------------
    # Retorna cargo dos vereadores da mesa no SPL
    # Para completar as informações usadas no RAMAIS -- com os cargos dos vereadores que fazem parte da mesa executiva
    # ----------------------------------------------------------------------------------------------------------------
    def get_spl_cargos_mesa(self):
        vereadores_cargo_mesa = self.cons.consome_cargos_mesa()
        objetos_vereadores_cargo_mesa = []
        for line in objetos_vereadores_cargo_mesa:
            objetos_vereadores_cargo_mesa.append(Vereadores_cargo_mesa(line['matricula'], line['ini_nome'],
                                                                       line['crg_nome'], line['crg_ordem']))
        return objetos_vereadores_cargo_mesa

