class Disciplina(object):
	def __init__(self,disciplina,completo=False):
		self.id = disciplina.getId()
		self.nome = disciplina.getNome()
		self.codigo = disciplina.getCodigo()
		self.id_departamento = disciplina.getId_departamento()
