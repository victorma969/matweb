angular.
	module('Modal').
		component('modalCampus',{
		templateUrl: 'app/Campus/modal.template.html'
		controller: ['MatWebGlobals','$uibModalInstance' function Box(uibModalInstance,MatWebGlobals){
		var ctrl = this;

		ctrl.cancelar = function () {
    	$uibModalInstance.dismiss('cancelar');
  		};

}]
	});