# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Campus import Campus as BDCampus
from Models.Campus.RespostaListar import RespostaListar

class Campus(Controller):

	def Listar(pedido_listar):
		return RespostaListar(BDCampus().pegarMultiplosCampus("WHERE nome = %s LIMIT %d OFFSET %d",(pedido_listar.getNome().replace(' ','%'),pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))