angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      console.log("Biscoito")
      var x = $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST' },

      });
      console.log(x);
      return x;
    }
]);
