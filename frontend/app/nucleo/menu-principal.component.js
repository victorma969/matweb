angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
       this.usuario_logado = MatWebGlobals.usuario;
    }]
  });