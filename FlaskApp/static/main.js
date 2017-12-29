(function () {

  'use strict';

  angular.module('webApp', [])

  .controller('webAppController', ['$scope', '$log', '$http',
    function($scope, $log, $http) {
    console.log("Angular")

     // fire the API request
    $scope.data = [];

    $scope.cleanData = function(responseData) {
        var cleanedData = []
        for(var i = 0; i < responseData['Location'].length; i++) {
            cleanedData[i] = {}
            for(var key in responseData) {
                cleanedData[i][key] = responseData[key][i].replace(/\b\w/g, l => l.toUpperCase());
            }
        }
        return cleanedData;
    };

    $http.post('/dataRequest').
      success(function(results) {
        console.log(results);
        $scope.data = $scope.cleanData(results);
        console.log($scope.data);
      }).
      error(function(error) {
        console.log(error);
      });

  }

  ]);

}());