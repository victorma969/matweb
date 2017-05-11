angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      return $resource('/api/Curso/:operacao', {}, {
        Cadastrar: { method: 'POST', params: {'operacao' : "Cadastrar"} },
      });
    }
  ]); 