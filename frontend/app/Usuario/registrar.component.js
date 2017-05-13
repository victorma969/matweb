angular.
  module('Usuario').
  component('usuarioRegistrar', {
    templateUrl: '/app/Usuario/cadastro.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Registrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','cor':'','nivel':'','conclusao':'','nomepai':'','nomemae':'','senha':''};
      this.registrar = function()
      {

   		}, function(erro){
   			this.erro = erro.data.mensagem
   		};
   	  }
    }]
  });