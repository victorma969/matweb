angular.
  module('Registrodesala').
  component('salaRegistrar', {
    templateUrl: '/app/Registrodesala/cadastrarsala.template.html',
    controller: ['ApiSala','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'predioName':'','corredorNumber':'','salaname':''};
      this.cadastrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Sala cadastrada com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
   	};
    }]
});
