angular.
  module('Registrodesala').
  factory('ApiSala', ['$resource',
    function($resource) {
      return $resource('/api/Registrodesala/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
