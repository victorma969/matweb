# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Disciplina import Disciplina as BDDisciplina
from Models.Disciplina.RespostaListar import RespostaListar

class Disciplina(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDDisciplina().pegarDisciplinas("WHERE id_departamento = %s AND nome LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdDepartamento()),pedido_listar.getNome().replace(' ','%'),str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))