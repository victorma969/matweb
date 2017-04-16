from Framework.BancoDeDados import BancoDeDados
from Database.Models.Professor import Professor as ModelProfessor


class Professor(object):
		
	def pegarProfessores(self, condicao, valores):
		professores = []
		for professor in BancoDeDados().consultarMultiplos("SELECT * FROM professor %s" % (condicao), valores):
			professores.append(ModelProfessor(professor))
		return professores
	
	def pegarProfessor(self, condicao, valores):
		return ModelProfessor(BancoDeDados().consultarUnico("SELECT * FROM professor %s" % (condicao), valores))
	
	def inserirProfessor(self, professor):
		BancoDeDados().executar("INSERT INTO professor ( nome ) VALUES ( %s ) RETURNING id", (professor.nome,))
		professor.id = BancoDeDados().pegarUltimoIDInserido()
		return professor
		
	def removerProfessor(self, professor):
		BancoDeDados().executar("DELETE FROM professor WHERE id = %s", (str(professor.id)))
		
	def alterarProfessor(self, professor):
		SQL = "UPDATE professor SET nome = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (professor.nome,professor.id))
