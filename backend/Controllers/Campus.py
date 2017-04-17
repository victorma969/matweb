# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Campus import Campus as BDCampus
from Models.Campus.RespostaListar import RespostaListar

class Campus(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDCampus().pegarMultiplosCampus("WHERE nome LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getNome().replace(' ','%'),str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))