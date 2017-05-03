class Campus(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.codigo = dados ['codigo']
			
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