angular.
  module('Aluno').
  component('alunoRegistrar', {
    templateUrl: '/app/Aluno/aluno.registrar.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;

      this.formulario = {};
      this.cadastrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
      } );
      }
    }]
  });
