class Horario(object):
	def __init__(self,horario):
		self.id = horario.getId()
		self.turno = horario.getTurno()
		self.hora_de_inicio = horario.getInicio()
		self.hora_de_termino = horario.getFim()
		self.dia_da_semana = horario.getDia()