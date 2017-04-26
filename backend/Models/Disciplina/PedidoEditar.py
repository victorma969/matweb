from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.nome = self.corpo['nome']
      self.codigo = self.codigo['codigo']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome
  
  def setCodigo(self,codigo):
    self.codigo = codigo
    
  def getCodigo(self):
    return self.codigo
