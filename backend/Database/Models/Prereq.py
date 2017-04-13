class Prereq(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.grupo = dados ['grupo']
			self.id_disc_pre = dados ['id_disc_pre']
			
	def getId(self):
		return self.id

	def setGrupo(self,grupo):
		self.grupo = grupo

	def getGrupo(self):
		return self.grupo
		
	def setId_disc_pre(self,id_disc_pre):
		self.id_disc_pre = id_disc_pre
	
	def getId_disc_pre(self):
		return self.id_disc_pre
