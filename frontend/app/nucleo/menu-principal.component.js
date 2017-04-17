angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
      console.log(typeof MatWebGlobals.usuario)
      if (typeof MatWebGlobals.usuario !== 'undefined') {
        this.perfil = MatWebGlobals.usuario;
      }else{
        this.perfil = ""
      }
       console.log(this.perfil)
    }]
  });