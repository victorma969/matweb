angular.
  module('Home').
  component('casaUsuario', {
    templateUrl: '/app/Home/home.template.html',
    controller: ['ApiHome', 'MatWebGlobals',function Entrar(ApiHome,MatWebGlobals) {
      this.nome_usuario = "";
	var ctrl = this;
	    }]
  });
