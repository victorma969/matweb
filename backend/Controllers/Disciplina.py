# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Disciplina import Disciplina as BDDisciplina
from Models.Disciplina.RespostaListar import RespostaListar

class Departamento(Controller):

	def Listar(pedido_listar):
		return RespostaListar(BDDisciplina().pegarDisciplinas("WHERE id_departamento = %d, nome = %s LIMIT %d OFFSET %d",(pedido_listar.getIdDepartamento(),pedido_listar.getNome().replace(' ','%'),pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))