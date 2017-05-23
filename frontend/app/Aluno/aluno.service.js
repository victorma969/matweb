angular.
  module('Aluno').
  factory('ApiAluno', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/:operacao', {}, {
        Cadastrar: { method: 'POST', params: {: "Cadastrar"} },
      });
    }
  ]);