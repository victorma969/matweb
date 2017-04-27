# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Horario import Horario as BDHorario
from Models.Horario.RespostaListar import RespostaListar
from Models.Horario.RespostaCadastrar import RespostaCadastrar
from Models.Horario.RespostaEditar import RespostaEditar
from Models.Horario.RespostaVer import RespostaVer
from Models.Horario.RespostaDeletar import RespostaDeletar
from Database.Models.Horario import Horario as ModelHorario

class Horario(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDHorario().pegarHorarios("",None))

	def Ver(self, pedido_ver):
		return RespostaVer(BDHorario().pegarHorarios("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		horario = ModelHorario()
		horario.setNome(pedido_cadastrar.getNome())
		return RespostaCadastrar(BDHorario().inserirHorario(horario))

	def Editar(self,pedido_editar):
		horario = BDHorario().pegarHorarios("WHERE id = %s ", (pedido_editar.getId()))
		horario.setNome(pedido_editar.getNome())
		BDHorario().alterarHorario(horario)
		return RespostaEditar("Horario Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		horario = BDHorario().pegarHorarios("WHERE id = %s ", (pedido_deletar.getId()))		
		BDHorario().removerHorario(horario)
		return RespostaDeletar("Horario Removido com sucesso!")
