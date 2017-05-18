angular.
  module('Departamento').
  component('listarDepartamento', {
    templateUrl: '/app/Departamento/departamento.template.html',
    controller: ['ApiDepartamento', 'MatWebGlobals',function Entrar(ApiDepartamento,MatWebGlobals) {
      this.nome_departamento = "";
	var ctrl = this;
	ctrl.departamentos = [];
      this.pesquisar = function()
      {
       	ApiDepartamento.Listar({id_campus: 1 , nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.departamentos = resultado.corpo
			console.log(ctrl.departamentos)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
});