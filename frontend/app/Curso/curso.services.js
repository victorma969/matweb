angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
        return $resource('/api/Curso/:operacao', {}, {
        Listar: { method: 'POST', params: {'operacao': "Listar"} }, 
        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} },
      });
    }
  ]);
