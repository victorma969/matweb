angular.
  module('Curso').
  component('ofertaCurso', {
    templateUrl: '/app/Curso/registrar.template.html',
    controller: ['ApiCurso', 'MatWebGlobals',function Entrar(ApiCurso,MatWebGlobals) {
      this.nome_curso = "";
      this.num = "ID do curso";
      this.departamento = "Departamento";
      this.cursos = "Cursos";
	var ctrl = this;
	ctrl.cursos = [];
      this.pesquisar = function()
      {
       	ApiCurso.Listar({id_departamento: 95 , nome: ctrl.nome_curso, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.cursos = resultado.corpo
			console.log(ctrl.cursos)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });

