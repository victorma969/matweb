# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Horario import Horario as BDHorario
from Models.Horario.RespostaListar import RespostaListar

class Horario(Controller):

	def Listar(pedido_listar):
		return RespostaListar(BDHorario().pegarHorarios("",None))