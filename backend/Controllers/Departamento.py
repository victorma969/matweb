# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Departamento import Departamento as BDDepartamento
from Models.Departamento.RespostaListar import RespostaListar

class Departamento(Controller):

	def Listar(pedido_listar):
		return RespostaListar(BDDepartamento().pegarDepartamentos("WHERE id_campus = %d, nome = %s LIMIT %d OFFSET %d",(pedido_listar.getIdCampus(),pedido_listar.getNome().replace(' ','%'),pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))