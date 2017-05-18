angular.
  module('Departamento').
  component('listarDepartamento', {
    templateUrl: '/app/Departamento/listar.template.html',
    controller: ['ApiDepartamento', 'MatWebGlobals',function Entrar(ApiDepartamento,MatWebGlobals) {
      this.nome_departamento = "";
      this.sigla_departamento = "Sigla";
  var ctrl = this;
  ctrl.departamento = [];
      this.pesquisar = function()
      {
        ApiCurso.Listar({sigla: ctrl.sigla_departamento, nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.departamento = resultado.corpo
      console.log(ctrl.cursos)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });