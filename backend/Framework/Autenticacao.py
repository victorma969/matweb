from Database.Controllers.RegistroLogin import RegistroLogin as DBRegistroLogin
from Database.Controllers.RegistroLogin import RegistroLogin as DBRegistroLogin
from Database.Models.RegistroLogin import RegistroLogin as ModelRegistroLogin
import uuid

class Autenticacao(object):

	@staticmethod
	def getUsuarioPeloTokenEIp(token,ip):
