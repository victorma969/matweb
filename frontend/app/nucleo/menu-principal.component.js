angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
      if (typeof MatWebGlobals.usuario !== 'undefined') {
        this.perfil = MatWebGlobals.usuario.perfil;
      }else{
        this.perfil = ""
      }
       console.log(this.perfil)
    }]
  });