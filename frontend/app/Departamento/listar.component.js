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
        ApiDepartamento.Listar({sigla: ctrl.sigla_departamento, nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.departamento = resultado.corpo
      console.log(ctrl.departamento)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });