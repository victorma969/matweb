
from Database.Controllers.Usuario import Usuario as BDUsuario

class Usuario(object):
	
	def Entrar(self,pedido_entrar):
		usuario = BDUsuario.getUsuarioPeloLogin(pedido_entrar.login)
		if(usuario.senha == pedido_entrar.senha):
			return RespostaEntrar(true)
		else:
			return RespostaEntrar(false)