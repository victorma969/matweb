from Framework.Resposta import Resposta
import json

class RespostaTestMethod(Resposta):

	def __init__(self,var1,var2):
		self.var1 = var1
		self.var2 = var2

	def getCabecalho(self):
		return [('Content-Type', 'application/json; charset=UTF-8'),('Content-Length', str(len(self.getCorpo())))]

	def getCorpo(self):
		return json.dumps(self)