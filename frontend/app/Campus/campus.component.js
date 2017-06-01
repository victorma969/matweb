angular.
  module('Campus').
  component('ofertaCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', 'MatWebGlobals','$uibModal',function Entrar(ApiCampus,MatWebGlobals,uibModal) {
  var ctrl = this;
  ctrl.campus = [];

    this.abrir = function(){
      var modalInstance = $uibModal.abrir({
      ariaLabelledBy: 'modal-title',
      ariaDescribedBy: 'modal-body',
      templateUrl: '/app/ModalCampus/modal.template.html',
      });
    }

        ApiCampus.Listar({ nome:"", pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.campus = resultado.corpo
      console.log(ctrl.campus)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      
    }]
  });
