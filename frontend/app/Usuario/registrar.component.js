angular.
  module('Usuario').
  component('usuarioRegistrar', {
    templateUrl: '/app/Usuario/registrar.template.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Registrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','conclusao':'','nome_pai':'','nome_mae':'','senha':'','cep':'','complemento':'','numero_telefone':'','numero_lote':'','id_raca_cor':'','
,'ano_conclusao':'','tipo_escola':''};
      this.cadastrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
      } );
      }
    }]
  });
