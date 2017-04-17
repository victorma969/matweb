from Framework.Controller import Controller
from Database.Controllers.Predio import Predio as BDPredio
from Models.Predio.RespostaListar import RespostaListar

class Predio(Controller):

	      def Listar(self,pedido_listar):
		      return RespostaListar(BDPredio().pegarPredios("WHERE id_campus = %d, nome = %s LIMIT %d OFFSET %d",(pedido_listar.getIdCampus(),"%".pedido_listar.getNome().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))
