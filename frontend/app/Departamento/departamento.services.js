  angular.
  module('Departamento').
  factory('ApiDepartamento', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/Listar', {}, {
        Listar: { method: 'POST' },
//        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} },
      });
    }
  ]);