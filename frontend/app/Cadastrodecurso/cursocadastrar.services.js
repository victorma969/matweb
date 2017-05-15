angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      return $resource('/api/Curso/:operaçao', {}, {
        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} },

      });
    }
  ]);
