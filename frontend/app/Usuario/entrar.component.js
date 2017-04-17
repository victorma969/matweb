angular.
  module('Usuario').
  component('usuarioEntrar', {
    templateUrl: '/app/Usuario/entrar.template.html',
    controller: ['ApiUsuario','$http', function Entrar(ApiUsuario,$http,$scope) {
      this.user = "Lucas";
      this.form = {};
      this.entrar = function(teste)
      {
       	var resultado = ApiUsuario.Entrar(this.form,function() {
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
   		}, function(){
   			console.log(resultado)
   		} );
   	  }
    }]
  });