class Usuario(object): 
	def __init__(self,usuario):
		self.id = usuario.getId()
		self.matricula = usuario.getMatricula()
        self.nome = usuario.getNome()
        self.cpf = usuario.getCpf()
        self.perfil = usuario.getPerfil()
