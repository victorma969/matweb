from Framework import Resposta
import json

class RespostaEntrar(Resposta):
	sucesso = None
	token = None

	def __init__(self,sucesso=False,token=None):
		self.sucesso = sucesso
		self.token = token

	def getCabecalho(self):
		return [('Content-Type', 'application/json; charset=UTF-8'),('Content-Length', str(len(self.getCorpo())))]

	def getCorpo(self):
		return json.dumps(self)