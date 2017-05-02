angular.
  module('Campus').
  component('ofertaCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', 'MatWebGlobals',function Entrar(ApiCampus,MatWebGlobals) {
      this.nome_campus = "";
  var ctrl = this;
  ctrl.campus_coco = [];
      this.pesquisar = function()
      {
        ApiCampus.Listar({id_campus: 4 , nome: ctrl.nome_campus, pagina: 0, quantidade: 4 },function(resultado) {
              ctrl.campus_coco = resultado.corpo
      console.log(ctrl.campus_coco)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });