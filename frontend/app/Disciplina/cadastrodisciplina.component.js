angular.
  module('CadrastoDisciplina').
  component('cadastrarDisciplina', {
    templateUrl: '/app/CadastroDisciplina/cadastrodisciplina.template.html',
    controller: ['ApiCadastroDisciplina','MatWebGlobals',function Cadastro(ApiCadastroDisciplina,MatWebGlobals) 
{
  
    var ctrl = this;
    this.formulario = {'id': '', 'nome':'', 'codigo': ''}
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