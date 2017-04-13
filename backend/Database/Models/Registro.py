class Resgistro(object):
		def __init__ (self.dados):
		if dados is not None:
			self.id = dados['id']
			self.token = dados['token']
			self.idusuario = dados['idsuario']
			self.ip = dados['ip']
			self.status = dados['status']
			pass
		
	def getId(self):
		return self.id

	def setToken(self,token):
		self.token = token
		
	def getToken(self):
		return self.token

	def setIdusuario (self,idusuario):
		self.idusuario = idusuario

	def getIdusuario (self):
		return self.idusuario
		
	def getIp (self):
		return self.ip

	def setIp(self,ip):
		self.ip = ip

	def getStatus(self):
		return self.status

	def setStatus(self, status):
		self.status = status