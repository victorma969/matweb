angular.
  module('Grade').
  component('usuarioDados', {
    templateUrl: '/app/Grade/grade.template.html',
    controller: ['ApiGrade', 'MatWebGlobals', '$scope', '$location', function Entrar(ApiGrade,MatWebGlobals,$scope,$location) {
        if (MatWebGlobals.hasOwnProperty('usuarioLogado')) {
            $scope.disciplinaUsuario = MatWebGlobals.usuarioLogado.disciplina;
            $scope.horarioUsuario = MatWebGlobals.usuarioLogado.horario;
        } else {
            $location.path('/Usuario/Entrar');
        }
        
  var ctrl = this;
  ctrl.grades = [];
        this.pesquisar = function()
      {
        ApiGrade.Listar({},function(resultado) {
              ctrl.grade = resultado.corpo
      console.log(ctrl.grades)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
});