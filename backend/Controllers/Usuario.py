
from Database.Controllers.Usuario import Usuario as BDUsuario

def temAcesso(metodo):
	return metodo
	
def Entrar(self,pedido_entrar):
	usuario = BDUsuario.getUsuarioPeloLogin(pedido_entrar.usuario)
	if(usuario.senha == pedido_entrar.senha):
		return RespostaEntrar(true)
	else:
		return RespostaEntrar(false)

def Sair(pedido_sair):
	pass