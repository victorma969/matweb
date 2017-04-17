# coding=utf-8
from Framework.Controller import Controller
from Framework.ErroNoHTTP import ErroNoHTTP
from Database.Controllers.Usuario import Usuario as BDUsuario
from Database.Controllers.Usuario import Usuario as BDUsuario
from Models.Usuario.RespostaEntrar import RespostaEntrar
import bcrypt
import uuid

class Usuario(Controller):

	@staticmethod
	def temAcesso(metodo,perfis):
		def metodo_com_acesso(self,pedido):
			usuario = Usuario.__getUsuarioPeloToken(pedido.variaveis_do_ambiente["AUTHORIZATION"])
			if usuario.getPerfil() in perfis:
				return metodo(self,pedido,usuario)
			else:
				ErroNoHTTP(403,"Acesso Negado!")
		return metodo_com_acesso
		
	def Entrar(self,pedido_entrar):
		usuario = BDUsuario().pegarUsuario("WHERE matricula = %s OR cpf = %s",(pedido_entrar.getLoginDoUsuario(),pedido_entrar.getLoginDoUsuario()))
		if usuario is not None:
			if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario().encode('utf-8'), usuario.getSenhaHashed().encode('utf-8')) == usuario.getSenhaHashed().encode('utf-8')):
				return RespostaEntrar(self.__gerarToken(usuario,pedido_entrar),{ 'nome': usuario.getNome(),'matricula': usuario.getMatricula(),'perfil': usuario.getPerfil(),'cpf': usuario.getCpf(),'id': usuario.getId(), })
			else:
				raise ErroNoHTTP(401,"Senha inválida!")
		else:
			raise ErroNoHTTP(401,"Usuário não encontrado!")

	def __gerarToken(self,usuario,pedido_entrar):
		return uuid.uuid4().hex

	@staticmethod
	def __getUsuarioPeloToken(token)
		registro_login = BDRegistroLogin().pegarRegistro("WHERE token = % AND entrada ",(token))
			if registro_login is None:
				ErroNoHTTP(401,"Você não está logado, ou sua sessão expirou!")
			else:
				return BDUsuario().pegarUsuario("WHERE id = %s",(id))

	def Sair(self,pedido_sair):
		pass

	def Listar(self,pedido_listar):
		usuarios = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_ver.getId()))

	def Ver(self,pedido_ver):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_ver.getId()))
		if usuario is not None:
			return None
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

	def Editar(self,pedido_editar):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_editar.getId()))
		if usuario is not None:
			usuario.set()
			BDUsuario().alterarUsuario(usuario)
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

	def AlterarSenha(self,pedido_alterar_senha):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_alterar_senha.getId()))
		if usuario is not None:
			usuario.setSenhaHashed(bcrypt.hashpw(pedido_alterar_senha.getNovaSenha().encode('utf-8'), bcrypt.gensalt()))
			BDUsuario().alterarUsuario(usuario)
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

