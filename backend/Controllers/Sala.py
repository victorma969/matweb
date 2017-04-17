from Framework.Controller import Controller
from Database.Controllers.Sala import Sala as BDSala
from Models.Sala.RespostaListar import RespostaListar

class Sala(Controller):

      def Listar(self,pedido_listar):
             		      return RespostaListar(BDSala().pegarSalas("WHERE id_predio = %s AND codigo = %s LIMIT %s OFFSET %s",(pedido_listar.getIdPredio(),"%".pedido_listar.getCodigo().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))
