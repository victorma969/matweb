angular.
  module('Aluno').
  component('usuarioRegistrar', {
    templateUrl: '/app/Aluno/cadastro.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','cor':'','nivel':'','conclusao':'','nome_pai':'','nome_mae':'','senha':''};
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