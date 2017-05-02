angular.
  module('Campus').
  factory('ApiCampus', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Listar', {}, {
        Listar: { method: 'POST' },

      });
    }
  ]);
