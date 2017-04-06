from Framework.BancoDeDados import BancoDeDados
from Database.Usuario import Usuario

class Usuario(object):
		
	def getUsuarioPeloMatriculaOuCPF(self,matricula_cpf):
		banco_de_dados = BancoDeDados()
		usuario = banco_de_dados.query(BancoDeDados.SQL("SELECT * FROM usuario WHERE matricula = %s OR cpf = %s",[matricula_cpf,matricula_cpf]))
		if usuario:
			return Usuario(usuario[0])
		else:
			return None