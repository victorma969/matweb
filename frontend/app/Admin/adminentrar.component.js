angular.
  module('Admin').
  component('adminEntrar', {
    templateUrl: '/app/Admin/entrar.template.html',
    controller: ['ApiAdmin','$http','$location', 'MatWebGlobals',function Entrar(ApiAdmin,$http,$location,MatWebGlobals) {
      this.formulario = {'usuario':'','senha':''};
      this.entrar = function()
      {
       	ApiAdmin.Entrar(this.formulario,function(resultado) {
          MatWebGlobals.usuarioLogado = resultado.corpo.usuario;
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
       		$location.path('/Admin')
   		}, function(erro){
   			this.erro = erro.data.mensagem
   		} );
   	  }
    }]
  });
