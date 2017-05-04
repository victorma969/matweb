angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      return $resource('/api/Curso/Listar', {}, {
        Cadastrar: { method: 'POST' },
        Editar: { method: 'POST' },
        Listar: { method: 'POST' },
        Excluir: { method: 'POST' },

      });
    }
  ]);
