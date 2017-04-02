from matwebdb import Matwebdb
from sql_statement import Sql_Statement

class Usuario(object):
		
#Initialization Method		
	def __init__(self, params=[], values=[]):
		self.values = values
		self.params = params
		self.set_attribs()

#Set User Attributes
	def set_attribs(self):
		count = 0
		while count < len(self.params):
			if self.params[count] == 'matricula':
				self.matricula = self.values[count]
			elif self.params[count] == 'nome':
				self.nome = self.values[count]
			elif self.params[count] == 'cpf':
				self.cpf = self.values[count]
			elif self.params[count] == 'curso':
				self.curso = self.values[count]
			elif self.params[count] == 'perfil':
				self.perfil = self.values[count]
			elif self.params[count] == 'senha':
				self.senha = self.values[count]
			count += 1

	def set_attribs_inverse(self):
		if hasattr(self,'matricula') == True:
			self.params.append('matricula')
			self.values.append(self.matricula)
		if hasattr(self,'nome') == True:
			self.params.append('nome')
			self.values.append(self.nome)
		if hasattr(self,'cpf') == True:
			self.params.append('cpf')
			self.values.append(self.cpf)
		if hasattr(self,'curso') == True:
			self.params.append('curso')
			self.values.append(self.curso)
		if hasattr(self,'perfil') == True:
			self.params.append('perfil')
			self.values.append(self.perfil)
		if hasattr(self,'senha') == True:
			self.params.append('senha')
			self.values.append(self.senha)
			
							
#Select User Method	
	def sel_user(self,registry=None):
		database = Matwebdb()
		if registry != None:
			sql_query = Sql_Statement('usuario',registry)
		else:
			sql_query = Sql_Statement('usuario')
		
		if len(self.params) == 0:
			self.set_attribs_inverse()
			
		result = database.query(sql_query.select(self.values,self.params))
		return result
		
#Insert User Method
	def insert_user(self):
		database = Matwebdb()
		sql_query = Sql_Statement('usuario')
		
		if len(self.params) == 0:
			self.set_attribs_inverse()
		
		database.insert(sql_query.insert(self.params,self.values))

#Update User Method
	def update_user(self,parameters,values):
		database = Matwebdb()
		sql_query = Sql_Statement('usuario')
		
		if len(self.params) == 0:
			self.set_attribs_inverse()
		
		database.update(sql_query.update(parameters,values,self.params[0],self.values[0]))