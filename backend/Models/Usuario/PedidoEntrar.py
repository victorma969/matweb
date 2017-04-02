from Framework import Pedido


class PedidoEntrar(Pedido):
	usuario = None
	senha = None

	def __init__(self,variaveis_do_ambiente):
		super(D, self).__init__(variaveis_do_ambiente)
		self.usuario = self.corpo.usuario
		self.senha = self.corpo.senha