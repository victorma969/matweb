from Database.Controllers.Disciplina import Disciplina

class Turma(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.letra = dados ['letra']
			self.id_disciplina = dados ['id_disciplina']
			
	def getId(self):
		return self.id

	def setLetra(self,letra):
		self.letra = letra

	def getLetra(self):
		return self.letra
		
	def setId_disciplina(self,disciplina):
		self.id_disciplina = (Disciplina().pegarDisciplina('nome = %s',(disciplina,))).getId()
	
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disciplina,))).getNome()
