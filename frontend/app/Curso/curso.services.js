angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {
<<<<<<< HEAD
      return $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST'},
=======
        return $resource('/api/Curso/:operacao', {}, {
        Listar: { method: 'POST', params: {'operacao': "Listar"} }, 
        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} },
>>>>>>> f80fe639810699e2156f30b85a7467289c349e30
      });
    }
  ]);