from Configuracao import Configuracao
import psycopg2


class BancoDeDados(object):
	
	def __init__(self):
		conf = Configuracao()
		self.conexao = psycopg2.connect(conf.configuracao['BancoDeDados']['StringDeConexao'])
		self.cursor = self.conexao.cursor()

	def query(self,SQL):
		self.cursor.execute(SQL)
		return self.cursor.fetchall()
	
	def query_with_args(self, SQL, data):
		self.cursor.execute(SQL %data)
		return self.cursor.fetchone()
			
	def execute(self, SQL, data):
		self.cursor.execute(SQL %data)
		self.conexao.commit()
	
	def __del__(self):
		self.conexao.close()	
