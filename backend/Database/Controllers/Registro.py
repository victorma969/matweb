from Framework.BancoDeDados import BancoDeDados
from Database.Models.Registro import Registro as ModelRegistro


class Registro(object):
		
	def pegarRegistro(self, condicao, valores):
		registro = []
		for registro in BancoDeDados().consultarMultiplos("SELECT * FROM registro %s" % (condicao), valores):
			registro.append(ModelRegistro(registro))
		return registro
	
	def pegarRegistro(self, condicao, valores):
		return ModelRegistro(BancoDeDados().consultarUnico("SELECT * FROM registro %s" % (condicao), valores))
	
	def inserirRegistro(self, registro):
		BancoDeDados().executar("INSERT INTO registro (id, token, idusuario, ip, status) VALUES (%s,%s,%s,%s,%s) RETURNING id", (registro.id, registro.token, registro.idusuario, registro.ip, registro.status))
		registro.id = BancoDeDados().pegarUltimoIDInserido()
		return registro
		
	def removerRegistro(self, registro):
		BancoDeDados().executar("DELETE FROM registro WHERE id = %s", (str(registro.id)))
		
	def alterarRegistro(self, registro):
		SQL = "UPDATE registro SET token = %s, idusuario = %s, ip = %s, status = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (registro.token, registro.idusuario, registro.ip, registro.status, registro.id))
