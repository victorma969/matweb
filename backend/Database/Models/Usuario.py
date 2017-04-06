from matwebdb import Matwebdb
from sql_statement import Sql_Statement

class Usuario(object):

	def __init__(self,dados):
		self.id = dados['id']
		self.nome = dados['nome']
		self.cpf = dados['cpf']
		self.senha = dados['senha']
		self.matricula = dados['matricula']
		self.perfil = dados['perfil']
		pass

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
