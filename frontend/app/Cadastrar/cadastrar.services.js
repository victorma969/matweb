angular.
  module('Cadastrar').
  factory('ApiDepartamentoRegistrar', ['$resource',
    function($resource) {
      return $resource('/api/Departamento/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
