angular.
  module('Aluno').
  component('alunoRegistrar', {
    templateUrl: '/app/Aluno/aluno.registrar.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;
      var nome
      var matricula
      var cpf
      var identidade
      var email
      var sexo
      var uf
      var id_raca_cor
      var ano_conclusao
      var nome_pai
      var nome_mae
      var senha
      var cep
      var complemento
      var numero_telefone
      var numero_lote
      var id_nivel
      var tipo_escola


      this.formulario = {nome: nome,matricula: matricula, cpf: cpf,identidade: identidade,email: email,sexo: sexo,uf: uf, Raca: Raca, id_nivel: id_nivel, ano_conclusao: ano_conclusao, nome_pai: nome_pai,nome_mae: nome_mae,senha: senha, cep: cep, complemento: complemento, numero_telefone: numero_telefone, numero_lote: numero_lote,
,ano_conclusao: ano_conclusao, tipo_escola: tipo_escola};
      this.cadastrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
   		};
   	  }
    }]
  });