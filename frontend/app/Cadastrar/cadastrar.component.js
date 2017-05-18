(function () {
'use strict';
angular
        .module('Cadastrar')
        .controller('registrarDepartamento', registrarDepartamento)
        templateUrl: '/app/Cadastrar/cadastrar.template.html',

    registrarDepartamento.$inject = ['ApiDepartamento', '$http', '$location', 'MatWebGlobals'];
    function registrarDepartamento(ApiDepartamento, $http, $location, MatWebGlobals) {
        var ctrl = this;
this.formulario = {'depName':'','idNumber':''};
        ctrl.cadastrar = cadastrar;

        function cadastrar() {
            ctrl.mensagem = true;
            UserService.Create(ctrl.formulario)
                .then(function (data) {
                    if (data.success) {
                        FlashService.Success('Registration successful', true);
                        $location.path('/Cadastrar');
                    } else {
                        FlashService.Error(data.message);
                        ctrl.mensagem = false;
                    }
                });
        }
    }

})();