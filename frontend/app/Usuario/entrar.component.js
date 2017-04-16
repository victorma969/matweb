angular.
  module('Usuario').
  component('Usuario-Entrar', {
    template: 'Hello, {{$ctrl.user}}!',
    controller: function GreetUserController() {
      this.user = 'world';
    }
  });