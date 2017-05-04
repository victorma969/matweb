angular.
  module('Curso').
  component('cursoRegistrar', {
    templateUrl: '/app/Curso/registrar.template.html',
    controller: ['ApiCurso','$http','$location', 'MatWebGlobals',function Registrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'.':'','.':'','.':''};
      this.registrar = function()
      {
        ApiCurso.Registrar(this.formulario,function(resultado) {
          //MatWebGlobals.usuarioLogado = resultado.corpo.usuario;
          $http.defaults.headers.common.Authorization = resultado.corpo.token;
          window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
          $location.path("/")
      }, function(erro){
        this.erro = erro.data.mensagem
      } );
      }
    }]
  });
