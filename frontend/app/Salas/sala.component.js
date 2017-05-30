angular.
  module('Sala').
  component('listarSalas', {
    templateUrl: '/app/Salas/sala.template.html',
    controller: ['ApiSalasApiSalasApiSalas', 'MatWebGlobals',function Entrar(ApiSalasApiSalas,MatWebGlobals) {
      this.nome_disciplina = "";
	var ctrl = this;
	ctrl.disciplinas = [];
      this.pesquisar = function()
      {
       	ApiSalas.Listar({id_departamento: 95, nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.disciplinas = resultado.corpo
			console.log(ctrl.disciplinas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
