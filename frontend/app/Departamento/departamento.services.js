angular.
  module('Departamento').
  factory('ApiDepartamento', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/:operaçao', {}, {
        Listar: { method: 'POST', params: {'operacao': "Listar" } },
      });
    }
  ]);
