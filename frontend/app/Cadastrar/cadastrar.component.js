angular.
module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamentoRegistrar','$http','$location', 'MatWebGlobals',function registrarDepartamento(ApiDepartamentoRegistrar,$http,$location,MatWebGlobals) {
        var ctrl = this;
        ctrl.cadastrar = cadastrar;
        function cadastrar() {
            ctrl.mensagem = true;
            ApiDepartamentoRegistrar.Cadastrar(ctrl.formulario)
                .then(function (data) {
                    if (data.success) {
                        MatWebGlobals.Success('Registration successful', true);
                        $location.path('/Cadastrar');
                    } else {
                        MatWebGlobals.Error(data.mensagem);
                        ctrl.mensagem = false;
                    }
                })
          };
    }]
});