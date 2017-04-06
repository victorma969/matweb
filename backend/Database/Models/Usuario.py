from matwebdb import Matwebdb


class Usuario(object):

	def __init__(self,dados):
		self.id = dados['id']
		self.nome = dados['nome']
		self.cpf = dados['cpf']
		self.senha = dados['senha']
		self.matricula = dados['matricula']
		self.perfil = dados['perfil']
		pass

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
