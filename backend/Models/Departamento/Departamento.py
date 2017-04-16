class Departamento(object):
	def __init__(self,campus):
		self.id = campus.getId()
		self.nome = campus.getNome()