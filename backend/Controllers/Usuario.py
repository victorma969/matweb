# coding=utf-8
from Framework.Controller import Controller
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
				return RespostaEntrar(True,"",self.__gerarToken(usuario),{ 'nome': usuario.getNome(),'matricula': usuario.getMatricula(),'perfil': usuario.getPerfil(),'cpf': usuario.getCpf(),'id': usuario.getId(), })
			else:
				return RespostaEntrar(False,"Senha inválida!")
		else:
			return RespostaEntrar(False,"Usuário não encontrado!")

	def __gerarToken(self,usuario):
		return "Biscoito"

def Sair(pedido_sair):
	pass
