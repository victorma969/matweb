class Usuario(object):

# O array com os dados do usuario devem seguir a seguinte ordem de parametros
#      dados = ['<id>','<matricula>','<nome>','<cpf>','<perfil>','<senha>']
#
# Para inclusao de usuarios, substituir '<id>' por None


	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados[0]
			self.matricula = dados[1]
			self.nome = dados[2]
			self.cpf = dados[3]
			self.perfil = dados[4]
			self.senha = dados[5]

	def getId():
		return self.id

	def setCpf(cpf):
		self.cpf = cpf
		
	def getCpf():
		return self.cpf

	def setMatricula(matricula):
		self.matricula = matricula
		
	def getMatricula():
		return self.matricula

	def setPerfil (perfil):
		self.perfil = perfil
		
	def getPerfil ():
		self.perfil

	def setNome(nome):
		self.nome = nome

	def getNome():
		return self.nome

	def getSenhaHashed():
		return self.senha

	def setSenhaHashed():
		return self.senha

	def setNome(nome):
		self.nome = nome

	def getNome():
		return self.nome

	def setNome(nome):
		self.nome = nome

	def getNome():
		return self.nome
