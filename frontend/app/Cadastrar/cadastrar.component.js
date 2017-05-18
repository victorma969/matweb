angular.
  module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamento','$http','$location', 'MatWebGlobals',function(ApiDepartamento,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'depName':'','idNumber':''};
      this.cadastrar = function()
      {
          ApiDepartamento.cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Departamento cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
   	};
    }]
});
