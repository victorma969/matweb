angular.
  module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiSexo','$http','$location', 'MatWebGlobals',function(ApiSexo,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':''};
      this.cadastrar = function()
      {
          ApiSexo.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Sala cadastrada com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
