angular.
  module('Aluno').
  factory('ApiAluno', ['$resource',
    function($resource) {
      return $resource('/api/Aluno/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);