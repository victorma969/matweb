from Framework.Resposta import Resposta

class RespostaEntrar(Resposta):

	def __init__(self,token=None,usuario=None):
		self.token = token
		self.usuario = usuario