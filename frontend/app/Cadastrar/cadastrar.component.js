angular.
  module('Departamento').
  component('departamentoRegistrar', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamento','$http','$location', 'MatWebGlobals',function(ApiDepartamento,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'predioName':'','corredorNumber':''};
      this.cadastrar = function()
      {
          ApiSala.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Departamento cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
   	};
    }]
});
