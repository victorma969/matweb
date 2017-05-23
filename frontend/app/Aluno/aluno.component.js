angular.
  module('Aluno').
  component('alunoRegistrar', {
    templateUrl: '/app/Aluno/registrar.template.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function(ApiAluno,$http,$location,MatWebGlobals) {
      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','conclusao':'','nome_pai':'','nome_mae':'','senha':'','ano_conclusao':''};
      this.registrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});