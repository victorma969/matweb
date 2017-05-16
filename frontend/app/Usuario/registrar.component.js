angular.
  module('Usuario').
  component('usuarioRegistrar', {
    templateUrl: '/app/Usuario/cadastro.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Registrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','cor':'','nivel':'','conclusao':'','nome_pai':'','nome_mae':'','senha':'','cep':'','complemento':'','numero_telefone':'','numero_lote':'','id_raca_cor':'','
,'id_nivel':'','ano_conclusao':'','tipo_escola':''};
      this.registrar = function()
      {

   		}, function(erro){
   			this.erro = erro.data.mensagem
   		} );
   	  }
    }]
  });