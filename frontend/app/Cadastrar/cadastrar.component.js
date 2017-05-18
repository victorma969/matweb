angular.
  module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamento','$http','$location', 'MatWebGlobals',function(ApiDepartamento,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.cadastrar = cadastrar;
      this.formulario = {'depName':'','idNumber':''};
 function.cadastrar(){
  ctrl.mensagem = true;
  ApiDepartamento.Create(ctrl.formulario)
  .then(function (data)){ 
    if(data.success){
MatWebGlobals.Success('registro feito com sucesso', true);
$http.path('/Cadastrar');
} else{
  MatWebGlobals.Error(data.messagem)
ctrl.mensagem = false;
}
};

    }]
})
