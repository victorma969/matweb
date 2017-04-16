angular.
  module('Usuario').
  component('usuarioEntrar', {
    template: 'Hello, {{$ctrl.user}}!',
    controller: ['ApiUsuario','$http', function GreetUserController(ApiUsuario,$http) {
      this.user = "Lucas";
      var resultado = ApiUsuario.Entrar({ "usuario":"00743723223", "senha":"Biscoito" },function() {
       				$http.defaults.headers.common.Authorization = resultado.corpo.token;
       				console.log(resultado.corpo.token)
   				} );
    }]
  });