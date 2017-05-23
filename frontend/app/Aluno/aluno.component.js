angular.
  module('Aluno').
  component('alunoRegistrar', {
    templateUrl: '/app/Aluno/registrar.template.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function Cadastrar (ApiAluno,$http,$location,MatWebGlobals) {
      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','conclusao':'','nome_pai':'','nome_mae':'','senha':'','cep':'','complemento':'','numero_telefone':'','numero_lote':'','ano_conclusao':'','tipo_escola':''};
      this.registrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
      } );
      }
    }]
  });
