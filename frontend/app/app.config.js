angular.
  module('MatWeb').
  config(['$locationProvider', '$routeProvider', '$http'
    function config($locationProvider, $routeProvider, $http) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      
      $http.defaults.headers.common.Authorization = ""
      $http.defaults.headers.post = { 'Content-Type' : 'application/json; charset=UTF-8' }

      $routeProvider.
        when('/', {
          template: '<site-home></site-home>'
        }).
        when('/login', {
          template: '<usuario-login></usuario-login>'
        }).
        otherwise('/');
    }
  ]);