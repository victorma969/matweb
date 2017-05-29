angular.
  module('Home').
  component('casaUsuario', {
    templateUrl: '/app/Home/index.html',
    controller: ['ApiHome', 'MatWebGlobals', '$scope', function Entrar(ApiHome,MatWebGlobals,$scope) {
        if (MatWebGlobals.hasOwnProperty('usuarioLogado')) {
            $scope.nomeUsuario = MatWebGlobals.usuarioLogado.nome;
        } else {
            $location.path('/Usuario/Entrar');
        }
        
	var ctrl = this;
	ctrl.usuarios = [];
	      this.pesquisar = function()
      {
       	ApiHome.Listar({},function(resultado) {
		          ctrl.usuarios = resultado.corpo
			console.log(ctrl.usuarios)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });