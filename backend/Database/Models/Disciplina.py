from Database.Controllers.Departamento import Departamento

class Disciplina(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.codigo = dados ['codigo']
			self.id_departamento = dados ['id_departamento']
			self.nivel = dados ['nivel']
			self.ementa = dados ['ementa']
			self.creditos = dados ['creditos']
			
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def setCodigo(self,codigo):
		self.codigo = codigo
		
	def getCodigo(self):
		return self.codigo
		
	def setId_departamento(self,id_departamento):
		self.id_departamento = id_departamento

	def getId_departamento(self):
		return self.id_departamento
		
	def getDepartamento(self):
		return (Departamento().pegarDepartamento('id = %s',(self.id_departamento,))).getNome()
	
	def setNivel(self,nivel):
		self.nivel = nivel
		                       
	def getNivel(self):
		return self.nivel
	
	def setEmenta(self,ementa):
		self.ementa = ementa
		
        def getEmenta(self):
	        return self.ementa
	
	def setCreditos(self,creditos):
		self.creditos = creditos
		
	def getCreditos(self):
		return self.creditos
	
