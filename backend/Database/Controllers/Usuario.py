from Framework.BancoDeDados import BancoDeDados
from Database.Models.Usuario import Usuario as DBUsuario


class Usuario(object):
		
	def getUsuarioPeloMatricula(self,matricula):
		banco = BancoDeDados()
		SQL = "SELECT * FROM usuario WHERE matricula = '%s'"
		user = DBUsuario(banco.query_with_args(SQL,matricula))
		return user