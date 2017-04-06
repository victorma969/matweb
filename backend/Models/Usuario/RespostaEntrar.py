from Framework import Resposta

class RespostaEntrar(Resposta):

	def __init__(self,sucesso=False,mensagem=None,token=None,usuario=None):
		self.sucesso = sucesso
		self.token = token
		self.mensagem = mensagem
		self.usuario = usuario