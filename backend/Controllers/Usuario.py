# coding=utf-8
from Framework.Controller import Controller
from Framework.ErroNoHTTP import ErroNoHTTP
from Database.Controllers.Usuario import Usuario as BDUsuario
from Models.Usuario.RespostaEntrar import RespostaEntrar
import bcrypt

class Usuario(Controller):

	def temAcesso(metodo):
		return metodo
		
	def Entrar(self,pedido_entrar):
		usuario = BDUsuario().pegarUsuario("matricula = %s OR cpf = %s",(pedido_entrar.getLoginDoUsuario(),pedido_entrar.getLoginDoUsuario()))
		if usuario is not None:
			if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario().encode('utf-8'), usuario.getSenhaHashed().encode('utf-8')) == usuario.getSenhaHashed().encode('utf-8')):
				return RespostaEntrar(True,"",self.__gerarToken(usuario,pedido_entrar),{ 'nome': usuario.getNome(),'matricula': usuario.getMatricula(),'perfil': usuario.getPerfil(),'cpf': usuario.getCpf(),'id': usuario.getId(), })
			else:
				return RespostaEntrar(False,"Senha inválida!")
		else:
			return RespostaEntrar(False,"Usuário não encontrado!")

	def __gerarToken(self,usuario,pedido_entrar):
		return "Biscoito"

	def Sair(pedido_sair):
		pass

	def Listar(pedido_listar):
		usuarios = BDUsuario().pegarUsuario("id = %s",(pedido_ver.getId()))

	def Ver(pedido_ver):
		usuario = BDUsuario().pegarUsuario("id = %s",(pedido_ver.getId()))
		if usuario is not None:
			return None
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

	def Editar(pedido_editar):
		usuario = BDUsuario().pegarUsuario("id = %s",(pedido_editar.getId()))
		if usuario is not None:
			usuario.set()
			BDUsuario().alterarUsuario(usuario)
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

	def AlterarSenha(pedido_alterar_senha):
		usuario = BDUsuario().pegarUsuario("id = %s",(pedido_alterar_senha.getId()))
		if usuario is not None:
			usuario.setSenhaHashed(bcrypt.hashpw(pedido_alterar_senha.getNovaSenha().encode('utf-8'), bcrypt.gensalt()))
			BDUsuario().alterarUsuario(usuario)
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

