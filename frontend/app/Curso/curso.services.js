angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
        return $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST'},
//        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} },
      });
    }
  ]);
