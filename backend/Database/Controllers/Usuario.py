from Framework.BancoDeDados import BancoDeDados
from Database.Models.Usuario import Usuario as ModelUsuario


class Usuario(object):
		
	def pegarUsuarios(self, condicao, valores):
		usuarios = []
		for usuario in BancoDeDados().consultarMultiplos("SELECT * FROM usuario %s" % (condicao), valores):
			usuarios.append(ModelUsuario(usuario))
		return usuarios
	
	def pegarUsuario(self, condicao, valores):
		usuario = BancoDeDados().consultarUnico("SELECT * FROM usuario %s" % (condicao), valores)
		if usuario is not None:
			return ModelUsuario(usuario)
		else:
			return None
	
	def inserirUsuario(self, usuario):
		BancoDeDados().executar("INSERT INTO usuario (matricula, nome, cpf, perfil, senha, email, sexo, nome_pai, nome_mae, id_raca_cor, id_nivel, ano_conclusao, cep, numero_lote, complemento, numero_telefone, tipo_escola) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id", (usuario.matricula, usuario.nome, usuario.cpf, usuario.perfil, usuario.senha, usuario.email, usuario.sexo, usuario.nome_pai, usuario.nome_mae, usuario.id_raca_cor, usuario.id_nivel, usuario.ano_conclusao, usuario.cep, usuario.numero_lote, usuario.complemento, usuario.numero_telefone, usuario.tipo_escola))
		usuario.id = BancoDeDados().pegarUltimoIDInserido()
		return usuario
		
	def removerUsuario(self, usuario):
		BancoDeDados().executar("DELETE FROM usuario WHERE id = %s", (str(usuario.id)))
		
	def alterarUsuario(self, usuario):
		SQL = "UPDATE usuario SET matricula = %s, nome = %s, cpf = %s, perfil = %s, senha = %s email = %s sexo = %s nome_pai = %s nome_mae = %s id_raca_cor = %s id_nivel = %s ano_conclusao = %s cep = %s numero_lote = %s complemento = %s numero_telefone = %s tipo_escola = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (usuario.matricula, usuario.nome, usuario.cpf, usuario.perfil, usuario.senha, usuario.email, usuario.sexo, usuario.nome_pai, usuario.nome_mae, usuario.id_raca_cor, usuario.id_nivel, usuario.ano_conclusao, usuario.cep, usuario.numero_lote, usuario.complemento, usuario.numero_telefone, usuario.tipo_escola usuario.id))