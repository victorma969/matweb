angular.
  module('Cadastrarcurso').
  factory('ApiRegistroCurso', ['$resource',
    function($resource) {
      return $resource('/api/Predio/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
