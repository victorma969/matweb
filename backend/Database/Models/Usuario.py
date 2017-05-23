class Usuario(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados['id']
			self.nome = dados['nome']
			self.matricula = dados['matricula']
			self.cpf = dados['cpf']
			self.identidade = dados['identidade']
			self.perfil = dados['perfil']
			self.senha = dados['senha']
			self.email = dados['email']
			self.sexo = dados['sexo']
			self.nome_pai = dados['nome_pai']
			self.nome_mae = dados['nome_mae']
		#	self.id_raca_cor = dados['id_raca_cor']
		#	self.id_nivel = dados['id_nivel']
			self.ano_conclusao = dados['ano_conclusao']
		#	self.cep = dados['cep']
		#	self.numero_lote = dados['numero_lote']
		#	self.complemento = dados['complemento']
		#	self.numero_telefone = dados['numero_telefone']
		#	self.tipo_escola = dados['tipo_escola']

	def getId(self):
		return self.id

	def setCpf(self,cpf):
		self.cpf = cpf
		
	def getCpf(self):
		return self.cpf

	def setMatricula(self,matricula):
		self.matricula = matricula
		
	def getMatricula(self):
		return self.matricula

	def setIdentidade(self,identidade):
		self.identidade = identidade
		
	def getIdentidade(self):
		return self.identidade

	def setPerfil (self,perfil):
		self.perfil = perfil
		
	def getPerfil (self):
		return self.perfil

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def getSenhaHashed(self):
		return self.senha

	def setSenhaHashed(self,senha):
		self.senha = senha

	def getEmail(self):
		return self.email
	
	def setEmail(self,email):
		self.email = email

	def getSexo(self):
		return self.sexo

	def setSexo(self,sexo):
		self.sexo = sexo

	def getNome_pai(self):
		return self.nome_pai

	def setNome_pai(self,nome_pai):
		self.nome_pai = nome_pai

	def getNome_mae(self):
		return self.nome_mae

	def setNome_mae(self,nome_mae):
		self.nome_mae = nome_mae

#	def getId_raca_cor(self):
#		return self.raca_cor	

#	def setId_raca_cor(self,id_raca_cor):
#		self.id_raca_cor = id_raca_cor
	
#	def getId_nivel(self):
#		return self.nivel

#	def setNivel(self,nivel):
#		self.nivel = nivel

	def getAno_conclusao(self):
		return self.ano_conclusao

	def setAno_conclusao(self,ano_conclusao):
		self.ano_conclusao = ano_conclusao

#	def getCep(self):
#		return self.cep

#	def setCep(self,cep):
#		self.cep = cep

#	def getNumero_lote(self):
#		return self.numero_lote

#	def setNumero_lote(self,numero_lote):
#		self.numero_lote = numero_lote

#	def getComplemento(self):
#		return self.complemento

#	def setComplemento(self,complemento):
#		self.complemento = complemento
	
#	def getNumero_telefone(self):
#		return self.numero_telefone

#	def setNumero_telefone(self,numero_telefone):
#		self.numero_telefone = numero_telefone

#	def getTipo_escola(self):
#		return self.tipo_escola

#	def setTipo_escola(self,tipo_escola):
#		self.tipo_escola = tipo_escola