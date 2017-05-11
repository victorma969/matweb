angular.
  module('CadrastoDisciplina').
  component('cadastrarDisciplina', {
    templateUrl: '/app/CadastroDisciplina/disciplina.template.html',
    controller: ['ApiCadastroDisciplina','$http','$location', 'MatWebGlobals',function Cadastro(ApiCadastroDisciplina,$http,$location,MatWebGlobals) 
{
  
    var ctrl = this;
    this.formulario = //{'alguma coisa': '', 'outra coisa':''...}
    this.cadastrardisciplina = function()
    {

      ApiCadastroDisciplina.CadastrarDisciplina(ctrl.formulario, function(data)
      {
        ctrl.mensagem = "Cadastro de disciplina realizado com sucesso !";
      }, function(data){
        crtl.mensagem = "Erro ao cadastrar disciplina!";
                        }                       );

    }
}                ]
                                    });