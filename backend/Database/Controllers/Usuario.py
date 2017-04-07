from Framework.BancoDeDados import BancoDeDados
from Database.Models.Usuario import Usuario as DBUsuario


class Usuario(object):
		
	def getUsuarioPelaMatricula(self, matricula):
		banco = BancoDeDados()
		SQL = "SELECT * FROM usuario WHERE matricula = '%s'"
		user = DBUsuario(banco.query_with_args(SQL,matricula))
		return user
	
	def getUsuario(self, parametro, valor):
		banco = BancoDeDados()
		SQL = "SELECT * FROM usuario WHERE %s = '%s'"
		user = DBUsuario(banco.query_with_args(SQL, (parametro,valor)))
		return user
	
	def insertUsuario(self, user):
		banco = BancoDeDados()
		SQL = "INSERT INTO usuario (matricula, nome, cpf, perfil, senha) VALUES ('%s','%s','%s','%s','%s')"
		banco.execute(SQL, (user.matricula, user.nome, user.cpf, user.perfil, user.senha))
		
	def removeUsuario(self, user):
		banco = BancoDeDados()
		SQL = "DELETE FROM usuario WHERE id = %s"
		banco.execute(SQL, (user.id))
		
	def alteraUsuario(self, user, parametro, valor):
		banco = BancoDeDados()
		SQL = "UPDATE usuario SET %s = '%s' WHERE id = %s"
		banco.execute(SQL, (parametro, valor, user.id))