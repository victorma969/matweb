from Framework.Resposta import Resposta
from Models.Curso.Curso import Curso as ModelCurso
class RespostaListar(Resposta):

	def __init__(self,campus):
		self.corpo = []
		for um_campus in campus:
			self.corpo.append(ModelCurso(curso))
