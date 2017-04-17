angular.
  module('Usuario').
  component('usuarioEntrar', {
    templateUrl: '/app/Usuario/entrar.template.html',
    controller: ['ApiUsuario','$http', function Entrar(ApiUsuario,$http,$scope) {
      this.user = "Lucas";
      var resultado = ApiUsuario.Entrar({ "usuario":"00743723223", "senha":"Biscoito" },function() {
       				$http.defaults.headers.common.Authorization = resultado.corpo.token;
       				window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
       				console.log(resultado.corpo.token)
   				} );
      this.entrar = function(teste)
      {
      		console.log(this);
      }
    }]
  });