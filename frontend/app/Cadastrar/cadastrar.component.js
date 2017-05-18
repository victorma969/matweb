angular
module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamento','$http','$location', 'MatWebGlobals',function registrarDepartamento(ApiDepartamento,$http,$location,MatWebGlobals) {
        var ctrl = this;
       this.formulario = {'depName':'','idNumber':''};
        ctrl.cadastrar = cadastrar;

        function cadastrar() {
            ctrl.mensagem = true;
            ApiDepartamento.Create(ctrl.formulario)
                .then(function (data) {
                    if (data.success) {
                        MatWebGlobals.Success('Registration successful', true);
                        $location.path('/Cadastrar');
                    } else {
                        MatWebGlobals.Error(data.mensagem);
                        ctrl.mensagem = false;
                    }
                })
        }
  }];