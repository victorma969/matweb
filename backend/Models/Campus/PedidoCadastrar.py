from Framework.Resposta import Resposta
from Models.Campus.Campus import Campus as ModelCampus

class RespostaCadastrar(Resposta):

	def __init__(self,usuario):
		self.corpo = ModelCampus(usuario)