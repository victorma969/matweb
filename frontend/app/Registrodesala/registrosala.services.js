angular.
  module('Registrodesala').
  factory('ApiSala', ['$resource',
    function($resource) {
      return $resource('/api/Sala/Cadastrar/:operacao', {}, {
        Cadastrar: { method: 'POST', params: {'operacao' : "Cadastrar"} },
        Editar: { method: 'POST' },
        Listar: { method: 'POST' },
        Excluir: { method: 'POST' },
      });
    }
  ]);