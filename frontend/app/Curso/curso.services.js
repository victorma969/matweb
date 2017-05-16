angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      var x = $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST' },

      });
      console.log(x);
      return x;
    }
]);
