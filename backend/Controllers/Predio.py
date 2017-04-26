from Framework.Controller import Controller
from Database.Controllers.Predio import Predio as BDPredio
from Models.Predio.RespostaListar import RespostaListar

class Predio(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDPredio().pegarPredios("WHERE id_campus = %s AND nome LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdCampus(),"%".pedido_listar.getNome().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))

	def Ver(self, pedido_ver):     
		return RespostaVer(BDPredio().pegarPredio("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		campus = ModelPredio()
		campus.setNome(pedido_cadastrar.getNome())
		campus.setSigla(pedido_cadastrar.getSigla())
		campus.setLatitude(pedido_cadastrar.getLatitude())
		campus.setLongitude(pedido_cadastrar.getLongitude())
		return RespostaCadastrar(BDPredio().inserirPredio(predio))

	def Editar(self,pedido_editar):
		campus = BDPredio().pegarPredio("WHERE id = %s ", (pedido_editar.getId()))
		campus.setNome(pedido_editar.getNome())
		campus.setSigla(pedido_cadastrar.getSigla())
		campus.setLatitude(pedido_cadastrar.getLatitude())
		campus.setLongitude(pedido_cadastrar.getLongitude())
		BDPredio().alterarPredio(predio)
		return RespostaEditar("Predio Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		predio = BDPredio().pegarPredio("WHERE id = %s ", (pedido_deletar.getId()))		
		BDPredio().removerPredio(predio)
		return RespostaDeletar("Predio Removido com sucesso!")
