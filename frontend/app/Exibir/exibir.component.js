angular.
  module('Exibir').
  component('materiaInfo', {
    templateUrl: '/app/Exibir/exibir.template.html',
    controller: ['ApiExibir','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiExibir,$http,$location,MatWebGlobals,$scope) {
      $location.when('/Disciplina/:Info?id=/:codigo', {
            controller: 'PagesCtrl'
        });
      $MatWebGlobals.html5Mode(true);
    controller('PagesCtrl', function ($routeParams) {
        console.log($location.id, $location.nome);
    });
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
