angular.
  module('Usuario').
  component('usuarioEntrar', {
    templateUrl: '/app/Usuario/entrar.template.html',
    controller: ['ApiUsuario','$http', function Entrar(ApiUsuario,$http,$scope) {
      this.user = "Lucas";
      this.form = {'usuario':'','senha':''};
      this.entrar = function(teste)
      {
      	console.log(this.form)
       	var resultado = ApiUsuario.Entrar(this.form,function(result) {
       		console.log(result)
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
   		}, function(erro){
   			console.log(erro.data.mensagem)
   		} );
   	  }
    }]
  });