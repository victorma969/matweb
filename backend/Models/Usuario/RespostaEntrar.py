
class RespostaEntrar(object):
	sucesso = None
	token = None

	def __init__(self,sucesso=False,token=None):
		self.sucesso = sucesso
		self.token = token