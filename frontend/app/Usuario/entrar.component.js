angular.
  module('Usuario').
  component('usuarioEntrar', {
    templateUrl: '/app/Usuario/entrar.template.html',
    controller: ['ApiUsuario','$http','$location', 'usuarioLogado',function Entrar(ApiUsuario,$http,$location,usuarioLogado) {
      this.user = "Lucas";
      this.formulario = {'usuario':'','senha':''};
      this.entrar = function(teste)
      {
      	console.log(this.form)
       	ApiUsuario.Entrar(this.form,function(resultado) {
          usuarioLogado = resultado.corpo.usuario;
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
       		$location.path("/")
   		}, function(erro){
   			this.erro = erro.data.mensagem
   		} );
   	  }
    }]
  });