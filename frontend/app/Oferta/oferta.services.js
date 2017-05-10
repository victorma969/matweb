angular.
  module('Oferta').
  factory('ApiOferta', ['$resource',
    function($resource) {
      return $resource('/api/Disciplinas/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);
