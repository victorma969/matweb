class Usuario(object):

	def __init__(self,usuario):
		self.id = usuario.getId()
		self.nome = usuario.getNome()
		self.matricula = usuario.getMatricula()
		self.cpf = usuario.getCpf()
		self.perfil = usuario.getPerfil()