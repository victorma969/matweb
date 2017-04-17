from Framework.Resposta import Resposta
from Models.Disciplina.Disciplina import Disciplina as ModelDisciplina
class RespostaListar(Resposta):

	def __init__(self,sala):
		self.corpo = []
		for sala in salas:
			self.corpo.append(ModelSala(sala))
