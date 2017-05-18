angular.
  module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamento','$http','$location', 'MatWebGlobals',function registrarDepartamento(ApiDepartamento,$http,$location,MatWebGlobals) {
      var ctrl = this;
      ctrl.registrar = registrar;
      this.formulario = {'depName':'','idNumber':''};
 function.registrar()
  ctrl.mensagem = true;
  ApiDepartamento.Create(ctrl.formulario)
  .then(function (data){ 
    if(data.success){
MatWebGlobals.Success('registro feito com sucesso', true);
$http.path('/Cadastrar');
} else{
  MatWebGlobals.Error(data.messagem);
ctrl.mensagem = false;
}
});

    }]
}
