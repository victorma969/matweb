import psycopg2

class Matwebdb(object):
	
	def __init__(self):
		conn_string = "host='localhost' dbname='matweb' user='postgres' password='postgres'"
		self.connection = psycopg2.connect(conn_string)
		self.cursor = self.connection.cursor()
		
	def query(self,query):
		self.cursor.execute(query)
		return self.cursor.fetchall()
	
	def insert(self,query):
		self.cursor.execute(query)
		self.connection.commit()
	
	def update(self,query):
		self.cursor.execute(query)
		self.connection.commit()
		
	def __def__(self):
		self.connectio.close()
