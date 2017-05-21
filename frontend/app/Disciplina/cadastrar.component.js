angular.
  module('Disciplina').
  component('cadastrarDisciplina', {
    templateUrl: '/app/Disciplina/cadastrar.template.html',
    controller: ['ApiDisciplina', 'MatWebGlobals',function Cadastro(ApiDisciplina,MatWebGlobals){

    var ctrl = this;
    this.formulario = {'nome':'', 'codigo': '', 'id_departamento':''}
    this.campos = "";

    this.limparForm = function(){  
      ctrl.campos.$setPristine();
      ctrl.campos.$setUntouched();
    }
    
    this.cadastrardisciplina = function(){
      
      ctrl.campos.$setDirty();

      if(ctrl.campos.$invalid)
      return;

      console.log("Se funfo")

      ApiDisciplina.Cadastrar(ctrl.formulario, function(data){
        ctrl.mensagem = "Cadastro de disciplina realizado com sucesso !";
        console.log("Se foi cadastrado")
      }, function(data){
        crtl.mensagem = "Erro ao cadastrar disciplina!";
        console.log("Se n foi cadastrado")
      });

}
}]
  });