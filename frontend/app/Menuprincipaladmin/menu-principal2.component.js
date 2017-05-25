angular.
  module('nucleoadmin').
  component('menuPrincipal', {
    templateUrl: '/app/Menuprincipaladmin/menu-principal.template.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
      if (typeof MatWebGlobals.usuarioLogado !== 'undefined') {
        this.perfil = MatWebGlobals.usuarioLogado.perfil;
      }else{
        this.perfil = ""
      }
    }]
  });