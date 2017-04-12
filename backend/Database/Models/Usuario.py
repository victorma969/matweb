class Usuario(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados['id']
			self.matricula = dados['matricula']
			self.nome = dados['nome']
			self.cpf = dados['cpf']
			self.perfil = dados['perfil']
			self.senha = dados['senha']

	def getId(self):
		return self.id

	def setCpf(self,cpf):
		self.cpf = cpf
		
	def getCpf(self):
		return self.cpf

	def setMatricula(self,matricula):
		self.matricula = matricula
		
	def getMatricula(self):
		return self.matricula

	def setPerfil (self,perfil):
		self.perfil = perfil
		
	def getPerfil (self):
		self.perfil

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def getSenhaHashed(self):
		return self.senha

	def setSenhaHashed(self,senha):
		self.senha = senha