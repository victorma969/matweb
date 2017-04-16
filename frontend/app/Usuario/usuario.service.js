angular.
  module('Usuario').
  factory('Entrar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Entrar', {}, {
        Entrar: { method: 'POST' }
        Sair: { method: 'POST' }
        Cadastrar: { method: 'POST' }
        Editar: { method: 'POST' }
        Listar: { method: 'POST' }
        Excluir: { method: 'POST' }
      });
    }
  ]);