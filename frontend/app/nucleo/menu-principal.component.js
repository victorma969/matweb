angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
       this.perfil = MatWebGlobals.usuario.perfil;
       console.log(this.perfil)
    }]
  });