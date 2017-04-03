from ErroNoHTTP import ErroNoHTTP
import sys, traceback

class PontoDeInicio(object):

	def __init__(self,variaveis_do_ambiente):
		self.variaveis_do_ambiente = variaveis_do_ambiente
		try:
			self.realizarChecagens()
			self.executar()
		except ErroNoHTTP as erro_no_http:
			self.resposta = erro_no_http

	def checarMetodo(self):
		if(self.variaveis_do_ambiente['REQUEST_METHOD'] != "POST"):
			raise ErroNoHTTP(405)

	def checarTipoDeConteudo(self):
		if(self.variaveis_do_ambiente['CONTENT_TYPE'] != "application/json; charset=UTF-8"):
			raise ErroNoHTTP(415)

	def checarTamanhoDoCorpoDoPedido(self):	
		try:
			if(int(self.variaveis_do_ambiente['CONTENT_LENGTH']) <= 0):
				raise ErroNoHTTP(411)
		except ValueError:
			raise ErroNoHTTP(411)

	def checarURL(self,api):
		if(api != "api"):
			raise ErroNoHTTP(404)

	def ChecarTamanhoDaURL(self,caminho):
		if(len(caminho) < 4):
			raise ErroNoHTTP(404)

	def checarSeControllerEMetodoExistem(self,erro,caminho,metodo):
		traceback.print_exc(file=sys.stdout)
		if(str(erro) == ("'module' object has no attribute '"+metodo+"'") or str(erro) == ("No module named Controllers."+caminho)):
			raise ErroNoHTTP(404)
		else:
			raise ErroNoHTTP(500) 

	def realizarChecagens(self):
		self.checarMetodo()
		self.checarTipoDeConteudo()
		self.checarTamanhoDoCorpoDoPedido()

	def executar(self):
		try:
			caminho = self.variaveis_do_ambiente['PATH_INFO'].split('/')
			self.ChecarTamanhoDaURL(caminho)
			metodo = caminho[-1]
			controller = caminho[-2]
			self.checarURL(caminho[1])
			del caminho[-1]
			del caminho[1]
			del caminho[0]
			caminho = ".".join(caminho)
			print(caminho+" "+metodo)
			self.resposta = getattr(getattr(__import__('Controllers.'+caminho), controller)(), metodo)(getattr(__import__('Models.'+caminho+'.Pedido'+metodo), 'Pedido'+metodo)(self.variaveis_do_ambiente))
		except (ImportError, AttributeError) as erro:
			self.checarSeControllerEMetodoExistem(erro,caminho,metodo)

	def getStatusDaResposta(self):
		return self.resposta.getStatus()

	def getCorpoDaResposta(self):
		return self.resposta.getCorpo()

	def getCabecalhoDaResposta(self):
		return self.resposta.getCabecalho()