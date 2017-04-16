angular.
  module('Usuario').
  component('usuarioEntrar', {
    template: 'Hello, {{$ctrl.user.corpo.nome}}!',
    controller: ['ApiUsuario', function GreetUserController(ApiUsuario) {
      var user = ApiUsuario.Entrar({ "usuario":"00743723223", "senha":"Biscoito" },function() { console.log(user) } );
    }]
  });