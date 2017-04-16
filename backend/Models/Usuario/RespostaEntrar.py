from Framework.Resposta import Resposta

class RespostaEntrar(Resposta):

	def __init__(self,token=None,usuario=None):
		self.corpo = { 'token' : token , 'usuario' : usuario }