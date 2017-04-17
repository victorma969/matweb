from Framework.Resposta import Resposta
from Models.Ass_turma_sala_horario.Ass_turma_sala_horario import Ass_turma_sala_horario as ModelAss_turma_sala_horario
class RespostaListar(Resposta):

	def __init__(self,Ass_turma_sala_horarios):
		self.corpo = []
		for Ass_turma_sala_horario in Ass_turma_sala_horarios:
			self.corpo.append(ModelAss_turma_sala_horario(Ass_turma_sala_horario))
