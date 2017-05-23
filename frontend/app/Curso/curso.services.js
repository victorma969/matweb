angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {

      return $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST' },
      });
      console.log(x);
      return x;
    }
]);