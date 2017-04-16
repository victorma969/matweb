angular.
  module('MatWeb').
  config(['$locationProvider', '$routeProvider', '$http',
    function config($locationProvider, $routeProvider, $http) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      
      $http.defaults.headers.common.Authorization = ""
      $http.defaults.headers.post = { 'Content-Type' : 'application/json; charset=UTF-8' }

      $routeProvider.otherwise('/');
    }
  ]);