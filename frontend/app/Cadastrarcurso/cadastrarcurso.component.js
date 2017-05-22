angular.
  module('Cadastrarcurso').
  component('registrarCurso', {
    templateUrl: '/app/Cadastrarcurso/cadastrarcurso.template.html',
    controller: ['ApiRegistroCurso','$http','$location', 'MatWebGlobals',function(ApiRegistroCurso,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','codigo':'0','permanencia_minima':'','permanencia_maxima':'','creditos_formatura':'','creditos_optativos_concentracao':'','creditos_optativos_conexa':'','creditos_livres_maximo':''};
      this.cadastrar = function()
      {
          ApiRegistroCurso.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Sala cadastrada com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
