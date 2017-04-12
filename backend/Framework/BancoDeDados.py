from Configuracao import Configuracao
import atexit
import psycopg2


class BancoDeDados(object):
	
	conexao = None
	cursor = None

	def __init__(self):
		if(BancoDeDados.cursor.closed or conexao.closed != 0)
			self.fechar()
			BancoDeDados.conexao = psycopg2.connect(Configuracao.getConfiguracao('BancoDeDados')['StringDeConexao'])
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

	def fechar():
		BancoDeDados.cursor.close()
		BancoDeDados.conexao.close()
