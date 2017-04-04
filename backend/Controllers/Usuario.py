from Framework.Controller import Controller
from Database.Controllers.Usuario import Usuario as BDUsuario
from Database.Controllers.TokenDeAcesso import TokenDeAcesso

class Usuario(Controller):

	def temAcesso(metodo):
		return metodo
		
	def Entrar(self,pedido_entrar):
		usuario = BDUsuario.getUsuarioPeloMatricula(pedido_entrar.getLoginDoUsuario())
		# if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario(), usuario.getSenhaHashed()) == usuario.getSenhaHashed()):
		if(usuario.getSenhaHashed() == pedido_entrar.getSenhaDoUsuario())
			return RespostaEntrar(true,"Biscoito")
		else:
			return RespostaEntrar(false)

	def Sair(pedido_sair):
		pass