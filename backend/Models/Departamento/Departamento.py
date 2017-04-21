class Departamento(object):
	def __init__(self,departamento):
		self.id = departamento.getId()
		self.id_campus = departamento.getIdCampus()
		self.nome = departamento.getNome()