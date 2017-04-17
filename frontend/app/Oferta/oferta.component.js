angular.
  module('Oferta').
  component('ofertaCursos', {
    templateUrl: '/app/Oferta/oferta.template.html',
    controller: ['ApiOferta', 'MatWebGlobals',function Entrar(ApiOferta,MatWebGlobals) {
      this.nome_disciplina = "";
	this.disciplinas = [];
      this.pesquisar = function()
      {
       	ApiOferta.Listar({id_departamento: 95 , nome: this.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          this.disciplinas = resultado.corpo
			console.log(this.disciplinas)
		}, function(erro){
   			this.erro = erro.data.mensagem
			console.log(this.erro)
   		} );
   	  }
    }]
  });
