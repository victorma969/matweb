class PontoDeInicio(object):

	resposta = None

	def __init__(self,variaveis_do_ambiente):
		self.variaveis_do_ambiente = variaveis_do_ambiente
		try:
			self.realizarChecagens()
			self.executar()
		except ErroNoHTTP as erro_no_http:
			self.resposta = erro_no_http

	def checarMetodo(self):
		if(self.variaveis_do_ambiente['REQUEST_METHOD'] != "POST"):

	def checarTipoDeConteudo(self):
		if(self.variaveis_do_ambiente['CONTENT_TYPE'] != "application/json; charset=UTF-8"):

	def checarTamanhoDoCorpoDoPedido(self)	
		if(int(self.variaveis_do_ambiente['CONTENT_LENGTH']) > 0):

	def realizarChecagens(self):
		self.checarMetodo()
		self.checarTipoDeConteudo()
		self.checarTamanhoDoCorpoDoPedido()

	def executar(self):


	def getStatusDaResposta(self):
		return self.resposta.getStatus()

	def getCorpoDaResposta(self):
		return self.resposta.getCorpo()

	def getCabecalhoDaResposta(self):
		return self.resposta.getCabecalho()