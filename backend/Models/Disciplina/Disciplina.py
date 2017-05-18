class Disciplina(object):
	def __init__(self,disciplina):
		self.id = disciplina.getId()
		self.nome = disciplina.getNome()
		self.codigo = disciplina.getCodigo()
