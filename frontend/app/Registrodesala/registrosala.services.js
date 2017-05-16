angular.
  module('Registrodesala').
  factory('ApiSala', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Listar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
