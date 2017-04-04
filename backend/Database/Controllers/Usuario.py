from Framework.BancoDeDados import BancoDeDados
from Database.Usuario import Usuario

class Usuario(object):
		
	def getUsuarioPeloMatricula(self,matricula):
		banco_de_dados = BancoDeDados()
		return Usuario(banco_de_dados.query(sql.SQL("SELECT * FROM usuario WHERE matricula = {}").format(sql.Identifier(matricula))[0])