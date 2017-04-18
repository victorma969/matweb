from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEntrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEntrar, self).__init__(variaveis_do_ambiente)
		try:
			self.nome = self.corpo['nome']
			self.matricula = self.corpo['matricula']
			self.cpf = self.corpo['cpf']
			self.perfil = self.corpo['perfil']
			self.senha = self.corpo['senha']
		except:
			raise ErroNoHTTP(400)

	def getNome(self):
		return self.nome

	def getMatricula(self):
		return self.matricula

	def getCpf(self):
		return self.cpf

	def getPerfil(self):
		return self.perfil

	def getSenha(self):
		return self.senha