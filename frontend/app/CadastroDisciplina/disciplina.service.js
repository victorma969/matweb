angular.
  module('CadastroDisciplina').
  factory('ApiCadastroDisciplina', ['$resource',
    function($resource) {
      return $resource('/api/xxxxxxxx/:operacao', {}, {
        CadastrarDisciplinas: { method: 'POST', params: {'operacao': "CadastrarDisciplinas"} }
      });
    }
  ]);