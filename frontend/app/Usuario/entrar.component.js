angular.
  module('Usuario').
  component('usuarioEntrar', {
    template: 'Hello, {{$ctrl.user.corpo.nome}}!',
    controller: ['ApiUsuario', function GreetUserController(ApiUsuario) {
      this.user = ApiUsuario.Entrar({ "usuario":"00743723223", "senha":"Biscoito" });
    }]
  });