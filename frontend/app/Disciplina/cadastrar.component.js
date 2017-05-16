angular.
  module('Disciplina').
  component('cadastrarDisciplina', {
    templateUrl: '/app/Disciplina/cadastrar.template.html',
    controller: ['ApiDisciplina', 'MatWebGlobals',function Cadastro(ApiDisciplina,MatWebGlobals) 
{

    var ctrl = this;
    var nome_disciplin = "";
    var codigo_disciplin = "";
    this.formulario = {nome: nome_disciplin, codigo: codigo_disciplin, id_departamento: 95 }
    this.cadastrardisciplina = function()
    {
      console.log("Se funfo")

      ApiDisciplina.Cadastrar(ctrl.formulario, function(data)
      {
        ctrl.mensagem = "Cadastro de disciplina realizado com sucesso !";
        console.log("Se foi cadastrado")
      }, function(data){
        crtl.mensagem = "Erro ao cadastrar disciplina!";
        console.log("Se n foi cadastrado")
                        }                       );

    }
}                ]
                                    });