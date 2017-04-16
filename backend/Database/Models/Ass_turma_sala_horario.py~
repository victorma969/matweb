from Database.Controllers.Sala import Sala
from Database.Controllers.Turma import Turma
from Database.Controllers.Horario import Horario
from Database.Controllers.Disciplina import Disciplina

class Ass_turma_sala_horario(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_sala = dados ['id_sala']
			self.id_turma = dados ['id_turma']
			self.id_horario = dados ['id_horario']
			
	def getId(self):
		return self.id

	def setId_sala(self,codigo_sala):
		self.id_sala = (Sala().pegarSala('codigo = %s',(codigo_sala,))).getId()

	def getId_sala(self):
		return self.id_sala
		
	def getSala(self):
		return (Sala().pegarSala('id = %s',(self.id_sala,))).getNome()

	def setId_turma(self,turma,disciplina):
		id_disciplina = (Disciplina().pegarDisciplina('nome = %s',(disciplina,))).getId()
		self.id_turma = (Turma().pegarTurma('letra = %s AND id_disciplina = %s',(turma,id_disciplina))).getId()
		
	def getId_turma(self):
		return self.id_turma
	
	def getTurma(self):
		return (Turma().pegarTurma('id = %s',(self.id_turma,))).getLetra()
		
	def setId_horario(self,turno,inicio,dia):
		self.id_horario = (Horario().pegarHorario('turno = %s AND inicio = %s AND dia= %s',(turno,inicio,dia))).getId()
		
	def getId_horario(self):
		return self.id_horario