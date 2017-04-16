angular.
  module('Usuario').
  component('usuarioEntrar', {
    template: 'Hello, {{$ctrl.user}}!',
    controller: ['ApiUsuario','$httpProvider', function GreetUserController(ApiUsuario,$httpProvider) {
      this.user = "Lucas";
      var resultado = ApiUsuario.Entrar({ "usuario":"00743723223", "senha":"Biscoito" },function() {
       				$httpProvider.defaults.headers.common.Authorization = resultado.corpo.token;
       				console.log(resultado.corpo.token)
   				} );
    }]
  });