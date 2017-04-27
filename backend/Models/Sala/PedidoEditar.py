from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.codigo = self.corpo['codigo']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	def setCodigo(self,codigo):
		self.nome = nome

	def getCodigo(self):
		return self.codigo
