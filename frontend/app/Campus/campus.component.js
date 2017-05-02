angular.
  module('Campus').
  component('ofertaCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiOferta', 'MatWebGlobals',function Entrar(ApiOferta,MatWebGlobals) {
      this.nome_campus = "";
  var ctrl = this;
  ctrl.campus = [];
      this.pesquisar = function()
      {
        ApiOferta.Listar({id_campus: 95 , nome: ctrl.nome_campus, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.campus = resultado.corpo
      console.log(ctrl.campus)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });