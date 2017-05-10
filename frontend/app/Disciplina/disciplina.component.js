angular.
  module('Disciplina').
  component('cadastrarDisciplina', {
    templateUrl: // Colocar ,
    controller: ['ApiDisciplina','$http','$location', 'MatWebGlobals',function RegisterDisciplina(ApiDisciplina,$http,$location,MatWebGlobals) 
{

    var ctrl = this;
    this.formulario = //{'alguma coisa': '', 'outra coisa':''...}
    this.pesquisar = function()
    {

      ApiDisciplina.CadastrarDisciplinas(ctrl.formulario, function(data){
        ctrl.mensagem = "Cadastro de disciplina realizado com sucesso !";
      }, function(data){
        crtl.mensagem = "Erro ao cadastrar disciplina!";
      });

    }
}]
});