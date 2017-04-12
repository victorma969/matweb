from Framework.BancoDeDados import BancoDeDados
from Database.Models.Usuario import Usuario as ModelUsuario


class Usuario(object):
		
	def pegarUsuarios(self, condicao, valores, inicio=0, quantidade=0):
		usuarios = []
		for usuario in BancoDeDados().consultarMultiplos(("SELECT * FROM usuario WHERE %s" % (condicao)), valores)
			usuarios[] = ModelUsuario(usuario)
		return usuarios
	
	def pegarUsuario(self, condicao, valores):
		return ModelUsuario(BancoDeDados().consultarUnico("SELECT * FROM usuario WHERE %s" % (condicao), valores))
	
	def inserirUsuario(self, usuario):
		BancoDeDados().execute("INSERT INTO usuario (matricula, nome, cpf, perfil, senha) VALUES (%s,%s,%s,%s,%s) RETURNING id", (usuario.matricula, usuario.nome, usuario.cpf, usuario.perfil, usuario.senha))
		usuario.id = BancoDeDados().pegarUltimoIDInserido()
		return usuario
		
	def removerUsuario(self, user):
		BancoDeDados().execute("DELETE FROM usuario WHERE id = %s", (user.id))
		
	def alterarUsuario(self, usuario):
		SQL = "UPDATE usuario SET matricula = %s, nome = %s, cpf = %s, perfil = %s, senha = %s WHERE id = %s"
		BancoDeDados().execute(SQL, (usuario.matricula, usuario.nome, usuario.cpf, usuario.perfil, usuario.senha, usuario.id))
