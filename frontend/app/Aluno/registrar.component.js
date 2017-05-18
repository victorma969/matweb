angular.
  module('Aluno').
  component('alunoRegistrar', {
    templateUrl: '/app/Aluno/aluno.registrar.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;
      var n = "";
      var m = "":
      var c = "":
      var i = "":
      var e = "":
      var s = "":
      var u = "":

      this.formulario = {nome:n,'matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','cor':'','nivel':'','conclusao':'','nome_pai':'','nome_mae':'','senha':'','cep':'','complemento':'','numero_telefone':'','numero_lote':'','id_raca_cor':'','
,'id_nivel':'','ano_conclusao':'','tipo_escola':''e};
      this.cadastrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
   		};
   	  }
    }]
  });