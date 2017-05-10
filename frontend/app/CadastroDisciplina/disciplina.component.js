angular.
  module('CadrastoDisciplina').
  component('cadastrarDisciplina', {
    templateUrl: // Colocar ,
    controller: ['ApiCadastroDisciplina','$http','$location', 'MatWebGlobals',function RegisterDisciplina(ApiCadastroDisciplina,$http,$location,MatWebGlobals) 
{

    var ctrl = this;
    this.formulario = //{'alguma coisa': '', 'outra coisa':''...}
    this.pesquisar = function()
    {

      ApiCadastroDisciplina.CadastrarDisciplinas(ctrl.formulario, function(data){
        ctrl.mensagem = "Cadastro de disciplina realizado com sucesso !";
      }, function(data){
        crtl.mensagem = "Erro ao cadastrar disciplina!";
      });

    }
}]
});