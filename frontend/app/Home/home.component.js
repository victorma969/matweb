angular.
  module('Home').
  component('casaUsuario', {
    templateUrl: '/app/Home/index.html',
    controller: ['ApiHome', 'MatWebGlobals',function Entrar(ApiHome,MatWebGlobals) {
        console.log(MatWebGlobals);
      this.nome_usuario = "";
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