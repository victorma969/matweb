angular.
  module('Disciplina').
  component('editarDisciplina', {
    templateUrl: '/app/Disciplina/editar.template.html',
    controller: ['ApiDisciplina', 'MatWebGlobals',function Edit(ApiDisciplina,MatWebGlobals) {
     
	var ctrl = this;
	this.alterar = {'nome':'', 'codigo': '', 'id_departamento':'', 'id':''}
      this.editar = function(){

          console.log("ENTROU AQUI?")
       	ApiDisciplina.Editar(ctrl.alterar,function(data) {
		          ctrl.msg = "A disciplina foi editada com sucesso !";
			console.log("FOI?")
		}, function(data){
   			ctrl.msg = "Erro ao editar disciplina !";
			console.log("NÃO FOI ?")
   		} );
   	  }
    }]
  });