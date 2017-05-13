angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      return $resource('/api/Curso/:operaçao', {}, {
        Listar: { method: 'POST' },
        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} },

      });
    }
  ]);
