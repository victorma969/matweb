# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Disciplina import Disciplina as BDDisciplina
from Models.Disciplina.RespostaListar import RespostaListar

class Disciplina(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDDisciplina().pegarDisciplinas("WHERE id_departamento = %s AND nome LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdDepartamento()),"%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))
	
	def Ver(self, pedido_ver):
		return RespostaVer(BDDisciplina().pegarDiscina("WHERE id = %s ", (pedido_ver.getId())))
	
	def Cadastrar(self,pedido_cadastrar):
		disciplina = ModelDisciplin()
		disciplina.setNome(pedido_cadastrar.getNome())
		disciplina.setCodigo(pedido_cadastrar.getCodigo())
		return RespostaCadastrar(BDDisciplina().inserirDisciplina(disciplina))
	
	def Editar(self,pedido_editar):
		disciplina = BDDisciplina().pegarDisciplina("WHERE id = %s ", (pedido_editar.getId()))
		disciplina.setNome(pedido_editar.getNome())
		disciplina.setCodigo(pedido_editar.getCodigo())
		BDDisciplina().alterarDisciplina(disciplina)
		return RespostaEditar("Disciplina Editado com sucesso!")
	
	def Deletar(self,pedido_deletar):
		disciplina = BDDisciplina().pegarDisciplina("WHERE id = %s ", (pedido_deletar.getId()))		
		BDDisciplina().removerDisciplina(disciplina)
		return RespostaDeletar("Disciplina Removido com sucesso!")
