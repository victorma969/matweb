angular.
  module('Predio').
  component('listarPredio', {
    templateUrl: '/app/Predio/predio.template.html',
    controller: ['ApiPredio', 'MatWebGlobals',function Entrar(ApiPredio,MatWebGlobals) {
      this.nome_predio = "";
	var ctrl = this;
	ctrl.predio = [];
      this.pesquisar = function()
      {
       	ApiPredio.Listar({id_predio: 95 , nome: ctrl.nome_predio, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.predio = resultado.corpo
			console.log(ctrl.predio)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
