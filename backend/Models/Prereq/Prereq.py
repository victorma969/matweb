class Prereq(object):
	def __init__(self,dados=None):
		if dados is not None:
			self.disciplina = dados ['nome']
			self.prereq = dados ['prereq']
			self.grupo = dados ['grupo']