angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['usuarioLogado', function Menu(usuarioLogado) {
      console.log(this.usuarioLogado)
    }]
  });