
from Database.Controllers.Usuario import Usuario as BDUsuario
from Database.Controllers.TokenDeAcesso import TokenDeAcesso

class Usuario(Controller):

	def temAcesso(metodo):
		return metodo
		
	def Entrar(self,pedido_entrar):
		usuario = BDUsuario.getUsuarioPeloMatricula(pedido_entrar.getLoginDoUsuario())
		if usuario != None:
			if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario(), usuario.getSenhaHashed()) == usuario.getSenhaHashed()):
				return RespostaEntrar(true,"",self.__gerarToken(usuario),usuario)
			else:
				return RespostaEntrar(false,"Senha inválida!")
		else:
			RespostaEntrar(false,"Usuário não encontrado!")

	def __gerarToken(self,usuario):
		pass

def Sair(pedido_sair):
	pass
