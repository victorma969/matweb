from Framework.Resposta import Resposta
from Models.Grau.GRau import Grau as ModelGrau

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
