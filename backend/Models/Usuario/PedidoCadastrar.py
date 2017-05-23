from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.nome = self.corpo['nome']
			self.matricula = self.corpo['matricula']
			self.cpf = self.corpo['cpf']
			self.perfil = self.corpo['perfil']
			self.senha = self.corpo['senha']
			self.email = self.corpo['email']
			self.sexo = self.corpo['sexo']
			self.nome_pai = self.corpo['nome_pai']
			self.nome_mae = self.corpo['nome_mae']
		#	self.id_raca_cor = self.corpo['id_raca_cor']
		#	self.id_nivel = self.corpo['id_nivel']
			self.ano_conclusao = self.corpo['ano_conclusao']
		#	self.cep = self.corpo['cep']
		#	self.numero_lote = self.corpo['numero_lote']
		#	self.complemento = self.corpo['complemento']
		#	self.numero_telefone = self.corpo['numero_telefone']
		#	self.tipo_escola = self.corpo['tipo_escola']
		except:
			raise ErroNoHTTP(400)

	def getNome(self):
		return self.nome

	def getMatricula(self):
		return self.matricula

	def getCpf(self):
		return self.cpf

	def getPerfil(self):
		return self.perfil

	def getSenha(self):
		return self.senha
	
	def getEmail(self):
		return self.email
	
#	def getSexo(self):
#		return self.sexo

	def getNome_pai(self):
		return self.nome_pai

	def getNome_mae(self):
		return self.nome_mae

#	def getId_raca_cor(self):
#		return self.raca_cor	
	
#	def getId_nivel(self):
#		return self.nivel

	def getAno_conclusao(self):
		return self.ano_conclusao

#	def getCep(self):
#		return self.cep

#	def getNumero_lote(self):
#		return self.numero_lote

#	def getComplemento(self):
#		return self.complemento
	
#	def getNumero_telefone(self):
#		return self.numero_telefone
	
#	def getAno_conclusao(self):
#		return self.ano_conclusao

#	def getTipo_escola(self):
#		return self.tipo_escola	
		