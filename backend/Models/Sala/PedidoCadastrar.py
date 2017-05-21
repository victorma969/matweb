from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.codigo = self.corpo['codigo']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	def setCodigo(self,codigo):
		self.codigo = codigo

	def getCodigo(self):
		return self.codigo
