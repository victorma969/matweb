from Database.Controllers.RegistroLogin import RegistroLogin as DBRegistroLogin
from Database.Models.RegistroLogin import RegistroLogin as ModelRegistroLogin
import uuid

class Autenticacao(object):

	@staticmethod
	def getUsuarioPeloTokenEIpEValido(token,ip):
		token = DBRegistroLogin().pegarRegistro("WHERE token = %s AND ip = %s",(token,ip))
		if token is not None:
			return token.getUsuario()
		else
			return None

	@staticmethod
	def criarToken(usuario,ip):
		token = ModelRegistroLogin()
		token.setUsuario(usuario)
		token.setToken(uuid.uuid4().hex)
		token.setIp(ip)
		token = DBRegistroLogin().inserirRegistro(token)