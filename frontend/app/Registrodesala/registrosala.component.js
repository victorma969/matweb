angular.
  module('Sala').
  component('salaRegistrar', {
    templateUrl: '/app/Sala/cadastrarsala.template.html',
    controller: ['ApiSala','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'predio':'','corredor':'','nomedasala':''};
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
