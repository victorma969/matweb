angular.
  module('Sala').
  factory('ApiSalas', ['$resource',
    function($resource) {
      return $resource('/api/Salas/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);
