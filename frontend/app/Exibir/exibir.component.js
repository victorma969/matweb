angular.
  module('Exibir').
  component('materiaInfo', {
    templateUrl: '/app/Exibir/exibir.template.html',
    controller: ['ApiExibir', 'MatWebGlobals',function Entrar(ApiExibir,MatWebGlobals) {
if (MatWebGlobals.hasOwnProperty('usuarioOferta')) {
            $scope.idMateria = MatWebGlobals.usuarioOferta.id;
            $scope.codigoMateria = MatWebGlobals.usuarioOferta.codigo;
        } else {
            $location.path('/Sexo');
        }
      this.nome_disciplina = "";
  var ctrl = this;
  ctrl.disciplinas = [];
      this.pesquisar = function()
      {
        ApiExibir.Listar(this.formulario,function(resultado) {
          MatWebGlobals.usuarioOferta = resultado.corpo.oferta;
          $http.defaults.headers.common.Authorization = resultado.corpo.token;
      console.log(ctrl.disciplinas)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });