from Framework import Resposta

class RespostaEntrar(Resposta):

	def __init__(self,sucesso=False,token=None):
		self.sucesso = sucesso
		self.token = token