# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Departamento import Departamento as BDDepartamento
from Models.Departamento.RespostaListar import RespostaListar

class Departamento(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDDepartamento().pegarDepartamentos("WHERE id_campus = %s, nome LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdCampus()),pedido_listar.getNome().replace(' ','%'),str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))