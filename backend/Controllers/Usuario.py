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
			if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario(), usuario.getSenhaHashed()) == usuario.getSenhaHashed()):
				return RespostaEntrar(true,"",self.__gerarToken(usuario),{ 'nome': usuario.getNome(),'matricula': usuario.getMatricula(),'perfil': usuario.getPerfil(),'cpf': usuario.getCpf(),'id': usuario.getId(), })
			else:
				return RespostaEntrar(false,"Senha inválida!")
		else:
			RespostaEntrar(false,"Usuário não encontrado!")

	def __gerarToken(self,usuario):
		return "Biscoito"

def Sair(pedido_sair):
	pass
