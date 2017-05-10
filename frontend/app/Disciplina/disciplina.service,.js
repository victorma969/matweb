angular.
  module('Disciplina').
  factory('ApiDisciplina', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/:operacao', {}, {
        CadastrarDisciplinas: { method: 'POST', params: {'operacao': "CadastrarDisciplinas"} }
      });
    }
  ]);