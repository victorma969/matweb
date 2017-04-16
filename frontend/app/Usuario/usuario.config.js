angular.
  module('MatWeb').
  config(['$routeProvider',
    function config($locationProvider, $routeProvider, $http) {
      $routeProvider.
        when('/Usuario/Entrar', {
          template: '<usuario-entrar></usuario-entrar>'
        })
    }
  ]);