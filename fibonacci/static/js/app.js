'use strict';

var app = angular.module('FibonacciApp', []);


app.config(function($locationProvider,$interpolateProvider){
    $locationProvider.html5Mode({
              enabled:true
    });
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');


 });    

app.controller('FibonacciController', ['$http', function($http) {
      
      var fc = this
      fc.sequence = "";

      this.submit = function(){
      	fc.error_message = null
        fc.results = true
      	var body = {"sequence": fc.sequence};
      	var start = new Date();
      	$http.post('/', body).then(function(res){
      		var obj = res.data;
      		console.log("Server Response", obj);
      		fc.sequence_member = obj.sequence_member;
      		fc.time_taken = obj.time_taken;
      		var end = new Date();
      		fc.diff = end - start
      	}).catch(function(error){
      		fc.error_message = error.data.message;
      	});
      }



}]);