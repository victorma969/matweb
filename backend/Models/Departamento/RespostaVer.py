from Framework.Resposta import Resposta
from Models.Departamento.Departamento import Departamento as ModelDepartamento

class RespostaVer(Resposta):

	def __init__(self,campus):
		self.corpo = ModelCampus(campus)