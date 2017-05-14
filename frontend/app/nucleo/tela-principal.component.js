angular.
  module('nucleo').
  component('telaPrincipal', {
    $window.location.href = "../../MatWeb/index.html";
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {}]
  });
