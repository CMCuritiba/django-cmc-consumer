# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.db import connection  
from django.http import Http404
from django.views.generic import View

import datetime
from .msconsumer import MSCMCConsumer

#----------------------------------------------------------------------------------------------------------
# Classe genérica base para os serviços
#----------------------------------------------------------------------------------------------------------
class GenericCMCView(View):
	cons = MSCMCConsumer()
	
#----------------------------------------------------------------------------------------------------------
# Classe genérica SPL para os serviços
#----------------------------------------------------------------------------------------------------------
class GenericCMCSPLView(GenericCMCView):	
	pass

#----------------------------------------------------------------------------------------------------------
# Classe SPL que consome projetos de uma determinada pauta
#----------------------------------------------------------------------------------------------------------
class SPLReuniaoComissaoView(GenericCMCSPLView):

	def get(cls, self):
		return GenericCMCView.cons.consome_reuniao_comissao()