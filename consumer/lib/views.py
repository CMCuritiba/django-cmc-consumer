# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.db import connection  
from django.http import Http404

import datetime

#----------------------------------------------------------------------------------------------------------
# Classe genérica base para os serviços
#----------------------------------------------------------------------------------------------------------
class GenericCMCView():
	object_name = None

	def __init__(self):
		self.retorno = []

#----------------------------------------------------------------------------------------------------------
# Classe genérica SPL para os serviços
#----------------------------------------------------------------------------------------------------------
class GenericCMCSPLView(GenericCMCView):	

	def __init__(self):
		super().__init__()

#----------------------------------------------------------------------------------------------------------
# Classe SPL que consome projetos de uma determinada pauta
#----------------------------------------------------------------------------------------------------------
class SPLReuniaoComissaoView(GenericCMCSPLView):

	def __init__(self):
		super().__init__()

	def get(self, request):
		return msconsumer.consome_reuniao_comissao(request)