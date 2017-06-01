angular.
  module('Disciplina').
  component('disciplinaListar', {
    templateUrl: '/app/Disciplina/listar.template.html',
    controller: ['ApiDisciplina','$location', 'MatWebGlobals', '$scope', function Listar(ApiDisciplina,$location,MatWebGlobals,$scope) {
      this.formulario = {'id_departamento':'','nome':''};
      this.listar = function()
      {
       	ApiDisciplina.Listar(this.formulario,function(resultado) {
          MatWebGlobals.disciplinasListadas = resultado.corpo.disciplina;
          cosole.log(MatWebGlobals);
   		}, function(error){
            $scope.erro = error.data.mensagem;
            $scope.$digest();
   		} );
   	  }
    }]
  });
