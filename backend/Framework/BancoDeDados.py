from Configuracao import Configuracao
import atexit
import psycopg2


class BancoDeDados(object):

	conexao = None
	cursor = None
	SQL = sql.SQL

	def __init__(self):
		if conexao == None
			conexao = psycopg2.connect(Configuracao.getConfiguracao(['BancoDeDados'])['StringDeConexao'])
			cursor = conexao.cursor()
		
	def query(self,query):
		conexao.execute(query)
		return cursor.fetchall()
	
	def execute(self,query):
		self.cursor.execute(query)
		self.connection.commit()
		
	@atexit.register
	def fechar():
		conexao.close()