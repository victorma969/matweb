from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.nome = self.corpo['nome']
			self.sigla = self.corpo['sigla']
			self.latitude = self.corpo['latitude']
			self.longitude = self.corpo['longitude']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def setSigla(self,sigla):
		self.sigla = sigla
		
	def getSigla(self):
		return self.sigla
		
	def setLatitude(self,latitude):
		self.latitude = latitude
	
	def getLatitude(self):
		return self.latitude
		
	def setLongitude(self,longitude):
		self.longitude = longitude
	
	def getLongitude(self):
		return self.longitude
