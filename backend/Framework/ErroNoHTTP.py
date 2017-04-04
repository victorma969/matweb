class ErroNoHTTP(BaseException):

	mensagem = {
		400 : "Bad Request",
		404 : "Not Found",
		405 : "Method Not Allowed",
		411 : "Length Required",
		415 : "Unsupported Media Type",
		500 : "Internal Server Error",
	}

	def __init__(self,codigo):
		self.codigo = codigo

	def getStatus(self):
		return str(self.codigo)+" "+self.mensagem[self.codigo]

	def getCabecalho(self):
		return [('Content-Type', 'application/json; charset=UTF-8'),('Content-Length', str(len(self.getCorpo())))]

	def getCorpo(self):
		return '{ "codigo" : '+str(self.codigo)+' , "mensagem" : "'+self.mensagem[self.codigo]+'" }'

	def __str__(self):
		return self.getCorpo()
