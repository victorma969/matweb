from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			
			self.nome = self.corpo['nome']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	
	def getNome(self):
		return self.nome