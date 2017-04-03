#from Configuracao import configuracao
#import atexit
#import psycopg2

#conexao = psycopg2.connect(configuracao['BancoDeDados']['StringDeConexao'])
#cursor = conexao.cursor()
		
#def query(self,query):
#	conexao.execute(query)
#	return cursor.fetchall()
	
#def execute(self,query):
#	self.cursor.execute(query)
#	self.connection.commit()
		
#@atexit.register
#def fechar():
#	conexao.close()