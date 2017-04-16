angular.
  module('Usuario').
  config(['$routeProvider',
    function config($routeProvider) {
      $routeProvider.
        when('/Usuario/Entrar', {
          template: '<usuario-entrar></usuario-entrar>'
        })
    }
  ]);