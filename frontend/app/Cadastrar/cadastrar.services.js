angular.
  module('Cadastrar').
  factory('ApiDepartamento', ['$resource',
    function($resource) {
      return $resource('/api/Departamento/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
