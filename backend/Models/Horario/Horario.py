class Horario(object):
	def __init__(self,horario):
		self.id = horario.getId()
		self.turno = horario.getTurno()
		self.inicio = horario.getInicio()
		self.fim = horario.getFim()
		self.dia = horario.getDia()
