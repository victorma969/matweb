angular.
  module('Usuario').
  component('usuarioEntrar', {
    templateUrl: '/app/Usuario/entrar.template.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Entrar(ApiUsuario,$http,$location,MatWebGlobals) {
      if($http.defaults.headers.common.Authorization != null)
      {
        $location.path("/")
      }
      this.formulario = {'usuario':'','senha':''};
      this.entrar = function(teste)
      {
       	ApiUsuario.Entrar(this.form,function(resultado) {
          MatWebGlobals.usuarioLogado = resultado.corpo.usuario;
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
       		$location.path("/")
   		}, function(erro){
   			this.erro = erro.data.mensagem
   		} );
   	  }
    }]
  });