from Framework.Pedido import Pedido


class PedidoTestMethod(Pedido):
	usuario = None
	senha = None

	def __init__(self,variaveis_do_ambiente):
		super(D, self).__init__(variaveis_do_ambiente)
		self.var1 = self.corpo.var1
		self.var2 = self.corpo.var2