
from Database.Controllers.Usuario import Usuario as BDUsuario
from Database.Controllers.TokenDeAcesso import TokenDeAcesso

def temAcesso(metodo):
	return metodo
	
def Entrar(self,pedido_entrar):
	usuario = BDUsuario.getUsuarioPeloLogin(pedido_entrar.getLoginDoUsuario())
	if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario, usuario.getSenhaHashed()) == usuario.getSenhaHashed()):
		return RespostaEntrar(true,TokenDeAcesso.gerarTokenDeAcesso(usuario.getID(),pedido_entrar.getIP()))
	else:
		return RespostaEntrar(false)

def Sair(pedido_sair):
	pass