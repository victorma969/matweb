from Configuracao import Configuracao
import atexit
import psycopg2


class BancoDeDados(object):
	
	conexao = None
	cursor = None

	def __init__(self):
		if(BancoDeDados.conexao == None or BancoDeDados.cursor == None):
			self.abrir()
		elif(BancoDeDados.cursor.closed or conexao.closed != 0):
			self.fechar()
			self.abrir()

	def abrir(self):
			BancoDeDados.conexao = psycopg2.connect(Configuracao().getConfiguracao('BancoDeDados')['StringDeConexao'])
			BancoDeDados.cursor = BancoDeDados.conexao.cursor()

	def consultarUnico(self,SQL,dados):
		BancoDeDados.cursor.execute(SQL,dados)
		return BancoDeDados.cursor.fetchall()
	
	def consultarMultiplos(self, SQL, dados):
		BancoDeDados.cursor.execute(SQL,dados)
		return BancoDeDados.cursor.fetchone()
			
	def executar(self, SQL, dados):
		BancoDeDados.cursor.execute(SQL,dados)
		BancoDeDados.conexao.commit()

	def pegarUltimoIDInserido(self):
		return BancoDeDados.cursor.fetchone()[0]

	def fechar(self):
		BancoDeDados.cursor.close()
		BancoDeDados.conexao.close()
