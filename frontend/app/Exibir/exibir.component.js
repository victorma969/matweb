angular.
  module('Exibir').
  component('materiaInfo', {
    templateUrl: '/app/Exibir/exibir.template.html',
    controller: ['ApiExibir', 'MatWebGlobals',function Entrar(ApiExibir,MatWebGlobals) {
      var param1 = $MatWebGlobals.param1;
      var param2 = $MatWebGlobals.param2;
      this.nome_disciplina = "";
	var ctrl = this;
	ctrl.disciplinas = [];
      this.pesquisar = function()
      {
       	ApiExibir.Listar({id_departamento: 95, nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.disciplinas = resultado.corpo
			console.log(ctrl.disciplinas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
