class Sala(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.resp_sala = dados ['resp_sala']
			self.codigo = dados ['codigo']
			self.id_predio = dados ['id_predio']
			
	def getId(self):
		return self.id

	def setResp_sala(self,resp_sala):
		self.resp_sala = resp_sala

	def getResp_sala(self):
		return self.resp_sala

	def setCodigo(self,codigo):
		self.codigo = codigo
		
	def getCodigo(self):
		return self.codigo
		
	def setId_predio(self,id_predio):
		self.id_predio = id_predio
		
	def getId_predio(self):
		return self.id_predio
	