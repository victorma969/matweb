angular.
  module('Registrodesala').
  component('salaRegistrar', {
    templateUrl: '/app/Registrodesala/registrodesala.template.html',
    controller: ['ApiSala','$http','$location', 'MatWebGlobals',function(ApiSala,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'predioName':'','corredorNumber':'','salaname':''};
      this.cadastrar = function()
      {
          ApiSala.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Sala cadastrada com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
   	};
    }]
});
